---
name: skill-jax-patterns
description: JAX 中的函数式编程模式：何时以及如何使用 grad、jit、vmap 和 pmap
version: 1.0.0
phase: 3
lesson: 12
tags: [jax, functional-programming, autodiff, compilation, vectorization]
---

# JAX 函数式模式

JAX transform 纯函数。下面每种模式都遵循同一条规则：写一个接收输入并返回输出、没有副作用的函数。然后 transform 它。

## 四种 transforms

### grad：对函数求导

```python
grads = jax.grad(loss_fn)(params, x, y)
loss, grads = jax.value_and_grad(loss_fn)(params, x, y)
```

使用场景：优化需要梯度。
约束：函数必须返回标量。对非标量输出，使用 `jax.jacobian`。

### jit：编译函数

```python
fast_fn = jax.jit(f)
```

使用场景：函数会被多次调用，并且输入 shape 相同。
约束：不能有依赖 traced values 的 Python control flow。条件分支用 `jax.lax.cond`，循环用 `jax.lax.scan`。

### vmap：向量化函数

```python
batch_fn = jax.vmap(f, in_axes=(None, 0))
```

使用场景：你写了处理单个样本的函数，现在需要让它处理 batches。
`in_axes` 指定哪个参数轴参与 batch。`None` 表示不参与 batch（broadcast）。

### pmap：跨设备并行

```python
parallel_fn = jax.pmap(f, axis_name='devices')
```

使用场景：你有多个 GPU/TPU，并希望做数据并行。
在函数内部，`jax.lax.pmean(x, 'devices')` 会跨设备取平均。

## 组合规则

Transforms 可以组合。顺序很重要：

```python
per_example_grads = jax.jit(jax.vmap(jax.grad(loss_fn), in_axes=(None, 0, 0)))
```

从右往左读：对 loss_fn 求梯度，对样本做向量化，编译结果。

有效组合：
- `jit(grad(f))`：编译后的梯度计算
- `jit(vmap(f))`：编译后的 batch 计算
- `vmap(grad(f))`：逐样本梯度
- `pmap(jit(f))`：并行编译计算
- `grad(jit(f))`：编译函数的梯度（等价于 jit(grad(f))）

## 参数管理模式

JAX 参数是 pytrees（嵌套数组 dict）：

```python
params = {
    'layer1': {'w': jnp.zeros((784, 256)), 'b': jnp.zeros(256)},
    'layer2': {'w': jnp.zeros((256, 10)),  'b': jnp.zeros(10)},
}
```

一次性更新所有参数：
```python
params = jax.tree.map(lambda p, g: p - lr * g, params, grads)
```

统计参数量：
```python
n_params = sum(p.size for p in jax.tree.leaves(params))
```

## PRNG Key 管理

JAX 要求显式随机 keys：

```python
key = jax.random.PRNGKey(0)
key, subkey = jax.random.split(key)
noise = jax.random.normal(subkey, shape)
```

对多个随机操作，一次 split：
```python
keys = jax.random.split(key, n)
```

永远不要复用 key。使用前始终 split。

## 常见错误

1. **在 jit 内修改 arrays**：JAX arrays 是不可变的。使用 `x.at[i].set(v)` 替代 `x[i] = v`。

2. **在 jit 内使用 Python print**：`print` 在 tracing 阶段运行，不在执行阶段运行。使用 `jax.debug.print("{}", x)`。

3. **在 jit 内对 traced values 使用 Python if/for**：使用 `jax.lax.cond`、`jax.lax.switch`、`jax.lax.scan`、`jax.lax.fori_loop`。

4. **忘记 `.block_until_ready()`**：JAX 使用 async dispatch。benchmark 时调用 `.block_until_ready()` 等待真实完成。

5. **复用 PRNG keys**：两个使用同一 key 的操作会产生相同的“随机”值。始终 split。

6. **在 jitted functions 中使用全局状态**：全局变量会在 trace 时被捕获。tracing 后的变化不可见。把所有东西作为参数传入。

## 决策清单

1. 函数会被调用多次吗？添加 `@jax.jit`。
2. 需要梯度吗？用 `jax.grad` 或 `jax.value_and_grad` 包裹。
3. 它处理单个样本，但你有 batch 吗？用 `jax.vmap` 包裹。
4. 你有多个设备吗？用 `jax.pmap` 包裹。
5. 它使用随机性吗？显式传递 PRNG keys。
6. 它对 array values 使用 Python control flow 吗？替换为 `jax.lax` primitives。

## 什么时候使用 JAX

使用 JAX，当：
- 你需要逐样本梯度（差分隐私、Fisher information）
- 你在 TPU 上训练（JAX 是原生框架）
- 你需要高阶导数（Hessians、Jacobians）
- 你想把整个训练 step 编译成单个 kernel
- 你的团队在 Google DeepMind 或 Anthropic

使用 PyTorch，当：
- 你想要最大的生态（HuggingFace、torchvision、Lightning）
- 你优先考虑调试便利，而不是原始速度
- 你要部署到 NVIDIA GPUs，并使用 TorchServe/Triton
- 你要招聘（PyTorch 开发者更多）
- 你想快速迭代新架构
