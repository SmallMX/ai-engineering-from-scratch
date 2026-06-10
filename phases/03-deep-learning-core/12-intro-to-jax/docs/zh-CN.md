# JAX 入门

> PyTorch 会修改 tensors。TensorFlow 构建 graphs。JAX 编译纯函数。最后这一点会改变你思考深度学习的方式。

**类型：** Build
**语言：** Python
**先修：** Phase 03 Lessons 01-10，基础 NumPy
**时间：** ~90 分钟

## 学习目标

- 使用 JAX 的函数式 API（jax.numpy、jax.grad、jax.jit、jax.vmap）编写纯函数神经网络代码
- 解释 PyTorch eager mutation 和 JAX functional compilation 模型之间的关键设计差异
- 应用 jit 编译和 vmap 向量化，相比朴素 Python 加速训练循环
- 在 JAX 中训练一个简单网络，并和 PyTorch 的面向对象方法对比显式状态管理

## 问题

你已经知道如何用 PyTorch 构建神经网络。你定义一个 `nn.Module`，调用 `.backward()`，让优化器 step。它能工作。数百万人都在用它。

但 PyTorch 的 DNA 里有一个约束：它以 eager 方式在 Python 中逐个追踪操作。每次 `tensor + tensor` 都是一次单独的 kernel launch。每个训练 step 都会重新解释同一段 Python 代码。在你需要跨 2,048 个 TPU 训练一个 5400 亿参数模型之前，这没问题。到了那个规模，开销会杀死你。

Google DeepMind 用 JAX 训练 Gemini。Anthropic 用 JAX 训练 Claude。这些都不是小规模操作，而是地球上最大的神经网络训练运行之一。他们选择 JAX，是因为 JAX 把训练循环当作一个可编译程序，而不是一串 Python 调用。

JAX 是带有三种超能力的 NumPy：自动微分、到 XLA 的 JIT 编译、自动向量化。你写一个处理单个样本的函数。JAX 给你一个能处理 batch、计算梯度、编译为机器码并跨多设备运行的函数。所有这些都不需要改变原函数。

## 概念

### JAX 哲学

JAX 是一个函数式框架。没有类，没有可变状态，没有 `.backward()` 方法。取而代之的是：

| PyTorch | JAX |
|---------|-----|
| 带状态的 `nn.Module` class | 纯函数：`f(params, x) -> y` |
| `loss.backward()` | `jax.grad(loss_fn)(params, x, y)` |
| Eager execution | 通过 XLA JIT 编译 |
| `for x in batch:` 手写循环 | `jax.vmap(f)` 自动向量化 |
| `DataParallel` / `FSDP` | `jax.pmap(f)` 自动并行 |
| 可变的 `model.parameters()` | 不可变的数组 pytree |

这不是风格偏好，而是编译器约束。JIT 编译需要纯函数：同样输入总是产生同样输出，没有副作用。这个限制正是 100 倍加速成为可能的原因。

### jax.numpy：熟悉的表面

JAX 在加速器上重新实现了 NumPy API：

```python
import jax.numpy as jnp

a = jnp.array([1.0, 2.0, 3.0])
b = jnp.array([4.0, 5.0, 6.0])
c = jnp.dot(a, b)
```

同样的函数名。同样的 broadcasting 规则。同样的 slicing 语义。但 arrays 位于 GPU/TPU 上，每个操作都能被编译器追踪。

一个关键差异是：JAX arrays 是不可变的。不能写 `a[0] = 5`。要写：`a = a.at[0].set(5)`。这会别扭一周，然后你会理解：不可变性正是 `grad`、`jit` 和 `vmap` 这类 transformations 可组合的原因。

### jax.grad：函数式自动微分

PyTorch 把梯度附着在 tensors 上（`.grad`）。JAX 把梯度附着在函数上。

```python
import jax

def f(x):
    return x ** 2

df = jax.grad(f)
df(3.0)
```

`jax.grad` 接收一个函数，并返回一个计算梯度的新函数。没有 `.backward()` 调用。没有存储在 tensors 上的 computation graph。梯度只是另一个你可以调用、组合或 JIT 编译的函数。

这可以任意组合：

```python
d2f = jax.grad(jax.grad(f))
d2f(3.0)
```

二阶导数。三阶导数。Jacobians。Hessians。全部通过组合 `grad` 完成。PyTorch 也能做这件事（`torch.autograd.functional.hessian`），但它更像附加功能。在 JAX 中，这是地基。

约束是：`grad` 只适用于纯函数。函数内部不能随意 print（它们会在 tracing 阶段运行，而不是执行阶段）。不能修改外部状态。没有显式 key 管理就不能生成随机数。

### jit：编译到 XLA

```python
@jax.jit
def train_step(params, x, y):
    loss = loss_fn(params, x, y)
    return loss

fast_step = jax.jit(train_step)
```

第一次调用时，JAX 会 trace 函数，也就是记录发生了哪些操作，但不真正执行它们。然后它把这条 trace 交给 XLA（Accelerated Linear Algebra），这是 Google 面向 TPU 和 GPU 的编译器。XLA 会融合操作、消除冗余内存拷贝，并生成优化过的机器码。

后续调用会完全跳过 Python。编译后的代码以 C++ 速度在加速器上运行。

JIT 有帮助的场景：
- 训练 step（同一计算重复数千次）
- 推理（同一模型，不同输入）
- 任何会被多次调用且输入 shape 相似的函数

JIT 有害的场景：
- 带有依赖值的 Python control flow 的函数（例如 `if x > 0`，其中 x 是 traced array）
- 一次性计算（编译开销超过运行时间）
- 调试（tracing 会隐藏真实执行）

control flow 限制是真实存在的。`jax.lax.cond` 替代 `if/else`。`jax.lax.scan` 替代 `for` 循环。这些不是可选项，而是编译的代价。

### vmap：自动向量化

你写一个处理单个样本的函数：

```python
def predict(params, x):
    return jnp.dot(params['w'], x) + params['b']
```

`vmap` 把它提升为处理 batch 的函数：

```python
batch_predict = jax.vmap(predict, in_axes=(None, 0))
```

`in_axes=(None, 0)` 表示：不要对 `params` 做 batch（共享参数），对 `x` 的第 0 轴做 batch。没有手写 `for` 循环。没有 reshape。没有手动穿透 batch 维度。JAX 会找出 batch 维度，并向量化整个计算。

这不是语法糖。`vmap` 会生成融合后的向量化代码，比 Python 循环快 10-100 倍。而且它可以和 `jit`、`grad` 组合：

```python
per_example_grads = jax.vmap(jax.grad(loss_fn), in_axes=(None, 0, 0))
```

逐样本梯度。一行。在 PyTorch 中不靠技巧几乎做不到。

### pmap：跨设备数据并行

```python
parallel_step = jax.pmap(train_step, axis_name='devices')
```

`pmap` 会把函数复制到所有可用设备（GPU/TPU）上，并切分 batch。在函数内部，`jax.lax.pmean` 和 `jax.lax.psum` 会跨设备同步梯度。

Google 使用 `pmap`（以及它的后继 `shard_map`）跨数千个 TPU v5e 芯片训练 Gemini。编程模型是：写单设备版本，用 `pmap` 包起来，完成。

### Pytrees：通用数据结构

JAX 操作 “pytrees”，也就是 lists、tuples、dicts 和 arrays 的嵌套组合。你的模型参数就是一个 pytree：

```python
params = {
    'layer1': {'w': jnp.zeros((784, 256)), 'b': jnp.zeros(256)},
    'layer2': {'w': jnp.zeros((256, 128)), 'b': jnp.zeros(128)},
    'layer3': {'w': jnp.zeros((128, 10)),  'b': jnp.zeros(10)},
}
```

每个 JAX transformation：`grad`、`jit`、`vmap`，都知道如何遍历 pytrees。`jax.tree.map(f, tree)` 会把 `f` 应用于每个 leaf。这就是优化器一次性更新所有参数的方式：

```python
params = jax.tree.map(lambda p, g: p - lr * g, params, grads)
```

没有 `.parameters()` 方法。没有参数注册。tree 结构就是模型。

### 函数式 vs 面向对象

PyTorch 把状态存储在对象内部：

```python
class Model(nn.Module):
    def __init__(self):
        self.linear = nn.Linear(784, 10)

    def forward(self, x):
        return self.linear(x)
```

JAX 使用带显式状态的纯函数：

```python
def predict(params, x):
    return jnp.dot(x, params['w']) + params['b']
```

params 被传入。什么都不存储。什么都不修改。这让每个函数都可测试、可组合、可编译。它也意味着你要自己管理 params，或者使用 Flax、Equinox 这样的库。

### JAX 生态

JAX 给你 primitives。库给你易用性：

| Library | 角色 | 风格 |
|---------|------|------|
| **Flax** (Google) | 神经网络层 | 带显式状态的 `nn.Module` |
| **Equinox** (Patrick Kidger) | 神经网络层 | 基于 Pytree，Pythonic |
| **Optax** (DeepMind) | 优化器 + LR schedules | 可组合的 gradient transforms |
| **Orbax** (Google) | Checkpointing | 保存/恢复 pytrees |
| **CLU** (Google) | Metrics + logging | 训练循环工具 |

Optax 是标准优化器库。它把 gradient transformation（Adam、SGD、clipping）和参数更新分离，让组合变得很简单：

```python
optimizer = optax.chain(
    optax.clip_by_global_norm(1.0),
    optax.adam(learning_rate=1e-3),
)
```

### 什么时候使用 JAX vs PyTorch

| Factor | JAX | PyTorch |
|--------|-----|---------|
| TPU support | 一等支持（Google 两者都构建） | 社区维护（torch_xla） |
| GPU support | 好（通过 XLA 支持 CUDA） | 最强（原生 CUDA） |
| Debugging | 难（tracing + compilation） | 易（eager，可逐行） |
| Ecosystem | 偏研究（Flax、Equinox） | 巨大（HuggingFace、torchvision 等） |
| Hiring | 小众（Google/DeepMind/Anthropic） | 主流（到处都是） |
| Large-scale training | 更强（XLA、pmap、mesh） | 好（FSDP、DeepSpeed） |
| Prototyping speed | 较慢（函数式开销） | 更快（直接 mutate and go） |
| Production inference | TensorFlow Serving、Vertex AI | TorchServe、Triton、ONNX |
| Who uses it | DeepMind (Gemini)、Anthropic (Claude) | Meta (Llama)、OpenAI (GPT)、Stability AI |

诚实答案是：除非你有明确理由使用 JAX，否则用 PyTorch。这些理由包括：TPU 访问、需要逐样本梯度、超大规模多设备训练，或者你在 Google/DeepMind/Anthropic 工作。

### JAX 中的随机数

JAX 没有全局随机状态。每个随机操作都需要显式 PRNG key：

```python
key = jax.random.PRNGKey(42)
key1, key2 = jax.random.split(key)
w = jax.random.normal(key1, shape=(784, 256))
```

这开始很烦。但它保证了跨设备和跨编译的可复现性，而这是 PyTorch 的 `torch.manual_seed` 在多 GPU 设置下无法保证的属性。

## 构建它

### 第 1 步：设置和数据

我们将使用 JAX 和 Optax 在 MNIST 上训练一个 3 层 MLP。784 个输入，两个隐藏层，分别有 256 和 128 个神经元，10 个输出类别。

```python
import jax
import jax.numpy as jnp
from jax import random
import optax

def get_mnist_data():
    from sklearn.datasets import fetch_openml
    mnist = fetch_openml('mnist_784', version=1, as_frame=False, parser='auto')
    X = mnist.data.astype('float32') / 255.0
    y = mnist.target.astype('int')
    X_train, X_test = X[:60000], X[60000:]
    y_train, y_test = y[:60000], y[60000:]
    return X_train, y_train, X_test, y_test
```

### 第 2 步：初始化参数

没有 class。只有一个返回 pytree 的函数：

```python
def init_params(key):
    k1, k2, k3 = random.split(key, 3)
    scale1 = jnp.sqrt(2.0 / 784)
    scale2 = jnp.sqrt(2.0 / 256)
    scale3 = jnp.sqrt(2.0 / 128)
    params = {
        'layer1': {
            'w': scale1 * random.normal(k1, (784, 256)),
            'b': jnp.zeros(256),
        },
        'layer2': {
            'w': scale2 * random.normal(k2, (256, 128)),
            'b': jnp.zeros(128),
        },
        'layer3': {
            'w': scale3 * random.normal(k3, (128, 10)),
            'b': jnp.zeros(10),
        },
    }
    return params
```

手动完成 He initialization。一个 seed 分裂成三个 PRNG keys。每个权重都是嵌套 dict 中的不可变 array。

### 第 3 步：前向传播

```python
def forward(params, x):
    x = jnp.dot(x, params['layer1']['w']) + params['layer1']['b']
    x = jax.nn.relu(x)
    x = jnp.dot(x, params['layer2']['w']) + params['layer2']['b']
    x = jax.nn.relu(x)
    x = jnp.dot(x, params['layer3']['w']) + params['layer3']['b']
    return x

def loss_fn(params, x, y):
    logits = forward(params, x)
    one_hot = jax.nn.one_hot(y, 10)
    return -jnp.mean(jnp.sum(jax.nn.log_softmax(logits) * one_hot, axis=-1))
```

纯函数。Params 进去，prediction 出来。没有 `self`，没有存储状态。`loss_fn` 从零计算 cross-entropy：softmax、log、negative mean。

### 第 4 步：JIT 编译训练 step

```python
@jax.jit
def train_step(params, opt_state, x, y):
    loss, grads = jax.value_and_grad(loss_fn)(params, x, y)
    updates, opt_state = optimizer.update(grads, opt_state, params)
    params = optax.apply_updates(params, updates)
    return params, opt_state, loss

@jax.jit
def accuracy(params, x, y):
    logits = forward(params, x)
    preds = jnp.argmax(logits, axis=-1)
    return jnp.mean(preds == y)
```

`jax.value_and_grad` 在一次 pass 中同时返回 loss 值和梯度。`@jax.jit` decorator 会把两个函数都编译到 XLA。第一次调用之后，每个训练 step 都不会再触碰 Python。

### 第 5 步：训练循环

```python
optimizer = optax.adam(learning_rate=1e-3)

X_train, y_train, X_test, y_test = get_mnist_data()
X_train, X_test = jnp.array(X_train), jnp.array(X_test)
y_train, y_test = jnp.array(y_train), jnp.array(y_test)

key = random.PRNGKey(0)
params = init_params(key)
opt_state = optimizer.init(params)

batch_size = 128
n_epochs = 10

for epoch in range(n_epochs):
    key, subkey = random.split(key)
    perm = random.permutation(subkey, len(X_train))
    X_shuffled = X_train[perm]
    y_shuffled = y_train[perm]

    epoch_loss = 0.0
    n_batches = len(X_train) // batch_size
    for i in range(n_batches):
        start = i * batch_size
        xb = X_shuffled[start:start + batch_size]
        yb = y_shuffled[start:start + batch_size]
        params, opt_state, loss = train_step(params, opt_state, xb, yb)
        epoch_loss += loss

    train_acc = accuracy(params, X_train[:5000], y_train[:5000])
    test_acc = accuracy(params, X_test, y_test)
    print(f"Epoch {epoch + 1:2d} | Loss: {epoch_loss / n_batches:.4f} | "
          f"Train Acc: {train_acc:.4f} | Test Acc: {test_acc:.4f}")
```

10 个 epoch。约 97% 测试准确率。第一个 epoch 慢，因为 JIT 编译。第 2-10 个 epoch 很快。

注意缺少了什么：没有 `.zero_grad()`，没有 `.backward()`，没有 `.step()`。整个更新是一次组合函数调用。梯度被计算、被 Adam 转换、被应用到参数上，全部发生在 `train_step` 内。

## 使用它

### Flax：Google 标准

Flax 是最常见的 JAX 神经网络库。它把 `nn.Module` 加了回来，但使用显式状态管理：

```python
import flax.linen as nn

class MLP(nn.Module):
    @nn.compact
    def __call__(self, x):
        x = nn.Dense(256)(x)
        x = nn.relu(x)
        x = nn.Dense(128)(x)
        x = nn.relu(x)
        x = nn.Dense(10)(x)
        return x

model = MLP()
params = model.init(jax.random.PRNGKey(0), jnp.ones((1, 784)))
logits = model.apply(params, x_batch)
```

结构和 PyTorch 相同，但 `params` 与模型分离。`model.init()` 创建 params。`model.apply(params, x)` 运行 forward pass。model 对象没有状态。

### Equinox：Pythonic 替代方案

Equinox（Patrick Kidger）把模型表示为 pytrees：

```python
import equinox as eqx

model = eqx.nn.MLP(
    in_size=784, out_size=10, width_size=256, depth=2,
    activation=jax.nn.relu, key=jax.random.PRNGKey(0)
)
logits = model(x)
```

模型本身就是 pytree。不需要 `.apply()`。参数就是模型的 leaves。这更接近 JAX 的思维方式。

### Optax：可组合优化器

Optax 把 gradient transformation 和 update 解耦：

```python
schedule = optax.warmup_cosine_decay_schedule(
    init_value=0.0, peak_value=1e-3,
    warmup_steps=1000, decay_steps=50000
)

optimizer = optax.chain(
    optax.clip_by_global_norm(1.0),
    optax.adamw(learning_rate=schedule, weight_decay=0.01),
)
```

Gradient clipping、learning rate warmup、weight decay 都作为 transforms 链式组合。每个 transform 看到 gradients，修改它们，再传给下一个。没有巨大的单体 optimizer class。

## 交付它

**安装：**

```bash
pip install jax jaxlib optax flax
```

GPU 支持：

```bash
pip install jax[cuda12]
```

TPU（Google Cloud）：

```bash
pip install jax[tpu] -f https://storage.googleapis.com/jax-releases/libtpu_releases.html
```

**性能坑点：**

- 第一次 JIT 调用很慢（编译）。benchmark 前先 warm up。
- 避免在 JIT 内对 JAX arrays 使用 Python 循环。使用 `jax.lax.scan` 或 `jax.lax.fori_loop`。
- `jax.debug.print()` 可以在 JIT 内工作。普通 `print()` 不行。
- 使用 `jax.profiler` 或 TensorBoard 做 profile。XLA 编译可能隐藏瓶颈。
- JAX 默认预分配 75% GPU 内存。设置 `XLA_PYTHON_CLIENT_PREALLOCATE=false` 可禁用。

**Checkpointing：**

```python
import orbax.checkpoint as ocp
checkpointer = ocp.PyTreeCheckpointer()
checkpointer.save('/tmp/model', params)
restored = checkpointer.restore('/tmp/model')
```

**本课产出：**
- `outputs/prompt-jax-optimizer.md`：一个用于选择合适 JAX optimizer 配置的提示词
- `outputs/skill-jax-patterns.md`：一个覆盖 JAX 函数式模式的技能

## 练习

1. 给 MLP 添加 dropout。在 JAX 中，dropout 需要 PRNG key：把 key 传过 forward pass，并为每个 dropout 层 split key。比较使用和不使用 dropout 的测试准确率。

2. 使用 `jax.vmap` 为 32 张 MNIST 图片组成的 batch 计算逐样本梯度。计算每个样本的梯度范数。哪些样本梯度最大？为什么？

3. 把手写 forward 函数替换为通用的 `mlp_forward(params, x)`，让它适用于任意层数。使用 `jax.tree.leaves` 自动确定深度。

4. benchmark 带和不带 `@jax.jit` 的 training step。各计时 100 step。你的硬件上加速幅度有多大？第一次调用的编译开销是多少？

5. 通过组合 `optax.chain(optax.clip_by_global_norm(1.0), optax.adam(1e-3))` 实现 gradient clipping。分别使用和不使用 clipping 训练。绘制训练期间的 gradient norm，观察效果。

## 关键术语

| 术语 | 人们常说 | 实际含义 |
|------|----------|----------|
| XLA | “让 JAX 快的东西” | Accelerated Linear Algebra，一个编译器，会从 computation graph 融合操作并生成优化过的 GPU/TPU kernels |
| JIT | “Just-in-time compilation” | JAX 在第一次调用时 trace 函数，编译到 XLA，后续调用运行编译版本 |
| 纯函数 | “没有副作用” | 输出只依赖输入的函数，没有全局状态、没有 mutation、没有不带显式 keys 的随机性 |
| vmap | “自动 batching” | 把处理单个样本的函数转换为处理 batch 的函数，不需要重写 |
| pmap | “自动并行” | 把函数复制到多个设备上，并切分输入 batch |
| Pytree | “嵌套数组 dict” | JAX 能遍历和 transform 的任意嵌套结构：lists、tuples、dicts 和 arrays |
| Tracing | “记录计算” | JAX 用抽象值执行函数，构建 computation graph，而不计算真实结果 |
| 函数式自动微分 | “函数的 grad” | 通过转换函数来计算导数，而不是把梯度存储附着到 tensors 上 |
| Optax | “JAX 的优化器库” | 一个可组合的 gradient transformations 库：Adam、SGD、clipping、scheduling，都可以链式组合 |
| Flax | “JAX 的 nn.Module” | Google 的 JAX 神经网络库，在保持显式状态的同时添加 layer 抽象 |

## 延伸阅读

- JAX documentation: https://jax.readthedocs.io/：官方文档，包含 grad、jit 和 vmap 的优秀教程
- "JAX: composable transformations of Python+NumPy programs" (Bradbury et al., 2018)：解释设计哲学的原始论文
- Flax documentation: https://flax.readthedocs.io/：Google 的 JAX 神经网络库
- Patrick Kidger, "Equinox: neural networks in JAX via callable PyTrees and filtered transformations" (2021)：Flax 的 Pythonic 替代方案
- DeepMind, "Optax: composable gradient transformation and optimisation"：标准优化器库
- "You Don't Know JAX" (Colin Raffel, 2020)：T5 作者之一写的 JAX 坑点和模式实践指南
