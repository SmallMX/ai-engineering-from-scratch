# 终端与 Shell —— 命令详解手册

> 本文档是 `zh-CN.md` 的配套参考，逐条拆解课程中出现的每一个命令，解释每个参数的含义。
> 如果你对某条命令"知道怎么打，但不确定为什么这样写"，这份手册就是给你的。

---

## 目录

1. [基础导航命令](#1-基础导航命令)
2. [Piping（管道）与 Redirect（重定向）](#2-piping管道与-redirect重定向)
3. [后台进程管理](#3-后台进程管理)
4. [tmux 终端复用器](#4-tmux-终端复用器)
5. [系统与 GPU 监控](#5-系统与-gpu-监控)
6. [SSH 与文件传输](#6-ssh-与文件传输)
7. [AI 工作常用 Aliases](#7-ai-工作常用-aliases)
8. [常见 AI 终端模式](#8-常见-ai-终端模式)

---

## 1. 基础导航命令

### `echo $SHELL`

```bash
echo $SHELL
```

| 部分 | 含义 |
|------|------|
| `echo` | 打印后面的内容到终端 |
| `$SHELL` | 一个**环境变量**，存储了当前使用的 Shell 程序路径，例如 `/bin/zsh` 或 `/bin/bash` |

**输出示例：**
```text
/bin/zsh
```

**为什么需要它：** 不同 Shell 有细微差异。知道自己用的是哪个 Shell，后面配置文件（`.zshrc` 还是 `.bashrc`）才不会搞错。

---

### `cd` — 切换目录

```bash
cd ~/projects/ai-engineering-from-scratch
```

| 部分 | 含义 |
|------|------|
| `cd` | **C**hange **D**irectory，切换当前工作目录 |
| `~` | 家目录的快捷写法，等同于 `/Users/你的用户名`（macOS）或 `/home/你的用户名`（Linux） |
| `~/projects/...` | 家目录下的 `projects/ai-engineering-from-scratch` 文件夹 |

**常用变体：**

```bash
cd ..       # 返回上一级目录
cd -        # 返回上一次所在的目录（来回切换很方便）
cd          # 不带参数，直接回到家目录
```

---

### `pwd` — 显示当前目录

```bash
pwd
```

| 部分 | 含义 |
|------|------|
| `pwd` | **P**rint **W**orking **D**irectory，打印当前所在的完整路径 |

**输出示例：**
```text
/Users/LMX/projects/ai-engineering-from-scratch
```

---

### `ls -la` — 列出文件

```bash
ls -la
```

| 部分 | 含义 |
|------|------|
| `ls` | **L**i**s**t，列出目录内容 |
| `-l` | **长格式**显示，包括权限、所有者、文件大小、修改时间 |
| `-a` | 显示**所有**文件，包括以 `.` 开头的隐藏文件（如 `.git`、`.env`） |
| `-la` | 把 `-l` 和 `-a` 合在一起写 |

**输出示例：**
```text
drwxr-xr-x  12 LMX  staff   384 Jun 17 10:00 .
drwxr-xr-x   5 LMX  staff   160 Jun 17 09:00 ..
drwxr-xr-x  15 LMX  staff   480 Jun 17 10:00 .git
-rw-r--r--   1 LMX  staff  1024 Jun 17 10:00 README.md
-rw-r--r--   1 LMX  staff   256 Jun 17 10:00 .env
```

**各列含义：**

| 列 | 示例 | 含义 |
|----|------|------|
| 第 1 列 | `drwxr-xr-x` | 文件类型和权限。`d` = 目录，`-` = 普通文件；`rwx` = 读/写/执行 |
| 第 2 列 | `12` | 硬链接数 |
| 第 3 列 | `LMX` | 所有者 |
| 第 4 列 | `staff` | 所属用户组 |
| 第 5 列 | `384` | 文件大小（字节） |
| 第 6-8 列 | `Jun 17 10:00` | 最后修改时间 |
| 最后一列 | `.git` | 文件/目录名 |

---

### 快捷键

| 快捷键 | 作用 | 详细说明 |
|--------|------|----------|
| `Ctrl+R` | 反向搜索历史命令 | 按下后输入关键字，会自动匹配之前执行过的命令。再按一次 `Ctrl+R` 查看更早的匹配。找到后按 `Enter` 执行，按 `Ctrl+C` 取消 |
| `Ctrl+L` | 清屏 | 等同于 `clear` 命令，把终端屏幕清空（历史不会丢失，只是看不到了） |
| `Ctrl+C` | 中断当前命令 | 给正在运行的进程发送 `SIGINT` 信号，通常会导致程序立即终止 |
| `Ctrl+Z` | 挂起当前命令 | 把正在运行的进程放到后台**暂停**。之后用 `fg` 恢复运行，或用 `bg` 让它在后台继续运行 |

---

## 2. Piping（管道）与 Redirect（重定向）

### 核心概念

**管道 `|`**：把左边命令的输出（stdout），作为右边命令的输入（stdin）。你可以把多个命令像水管一样连起来。

**重定向 `>` `>>` `2>`**：把输出写入文件，而不是打印到屏幕。

```mermaid
graph LR
    A["命令 1 的输出"] -->|"管道 |"| B["命令 2 的输入"]
    B -->|"管道 |"| C["命令 3 的输入"]
    C -->|"重定向 >"| D["文件"]
```

---

### `cat train.log | grep "loss" | wc -l`

```bash
cat train.log | grep "loss" | wc -l
```

这条命令由 3 个命令通过管道连接而成，**从左到右逐步过滤**：

| 步骤 | 命令 | 作用 |
|------|------|------|
| 1 | `cat train.log` | `cat` = con**cat**enate，把 `train.log` 的全部内容输出 |
| 2 | `grep "loss"` | `grep` = **G**lobal **R**egular **E**xpression **P**rint。从输入中筛选出包含 `"loss"` 的行 |
| 3 | `wc -l` | `wc` = **W**ord **C**ount。`-l` 表示只计算**行数** |

**数据流：**
```text
train.log 全文 → 只留含 "loss" 的行 → 数这些行有几行 → 输出数字
```

**输出示例：** `42`（表示日志中有 42 行包含 "loss"）

---

### `grep "loss:" train.log | awk '{print $NF}' > losses.txt`

```bash
grep "loss:" train.log | awk '{print $NF}' > losses.txt
```

| 部分 | 含义 |
|------|------|
| `grep "loss:" train.log` | 从 `train.log` 中筛选出包含 `"loss:"` 的行 |
| `awk '{print $NF}'` | `awk` 是一个文本处理工具。`$NF` 表示每行的**最后一个字段**（`NF` = **N**umber of **F**ields，字段总数；`$NF` 就是取第 NF 个字段，即最后一个） |
| `> losses.txt` | 把结果写入 `losses.txt`，**覆盖**该文件原有内容 |

**举例：** 如果日志中有一行是 `Epoch 5 loss: 0.3421`，那 `awk '{print $NF}'` 会提取出 `0.3421`。

---

### `tail -f train.log | grep --line-buffered "ERROR"`

```bash
tail -f train.log | grep --line-buffered "ERROR"
```

| 部分 | 含义 |
|------|------|
| `tail` | 显示文件的**末尾**内容（默认最后 10 行） |
| `-f` | **f**ollow 模式——不退出，持续监控文件新增的内容（文件每写入一行就显示一行） |
| `grep --line-buffered "ERROR"` | 筛选出包含 `"ERROR"` 的行。`--line-buffered` 让 `grep` 在管道中每收到一行就立即输出，不缓存（否则在管道中可能看不到实时输出） |

**使用场景：** 训练正在跑的时候，实时监控是否出现错误日志。

---

### `grep "final_accuracy" results/*.log | sort -t= -k2 -n -r`

```bash
grep "final_accuracy" results/*.log | sort -t= -k2 -n -r
```

| 部分 | 含义 |
|------|------|
| `grep "final_accuracy" results/*.log` | 在 `results/` 目录下所有 `.log` 文件中搜索含 `"final_accuracy"` 的行 |
| `results/*.log` | Shell **通配符**，匹配 `results/` 下所有以 `.log` 结尾的文件 |
| `sort` | 排序命令 |
| `-t=` | 设置分隔符为 `=`（默认分隔符是空格/tab） |
| `-k2` | 按第 **2** 个字段排序（`=` 号后面的部分，即精度值） |
| `-n` | 按**数字**大小排序（而不是字母顺序，否则 `9` 会排在 `10` 后面） |
| `-r` | **逆序**排列（从大到小） |

**举例：** 假设日志中有 `final_accuracy=0.95`，用 `=` 切分后第二段是 `0.95`，按数字从大到小排。

---

### 重定向 stdout 和 stderr

```bash
python train.py > output.log 2> errors.log
```

| 部分 | 含义 |
|------|------|
| `python train.py` | 执行 Python 训练脚本 |
| `> output.log` | 把**标准输出**（stdout，文件描述符 `1`）写入 `output.log` |
| `2> errors.log` | 把**标准错误**（stderr，文件描述符 `2`）写入 `errors.log` |

> **什么是 stdout 和 stderr？**
> - **stdout**（标准输出）：程序正常的输出内容，比如 `print()` 打印的东西
> - **stderr**（标准错误）：程序的错误信息和警告，比如 Python 的 traceback

```bash
python train.py > train_full.log 2>&1
```

| 部分 | 含义 |
|------|------|
| `> train_full.log` | stdout 写入 `train_full.log` |
| `2>&1` | 把 stderr（`2`）重定向到 stdout（`1`）当前指向的位置。因为 stdout 已经指向 `train_full.log`，所以 stderr 也会写入同一个文件 |

> **`&1` 中的 `&` 是什么意思？**  
> `&` 表示后面的 `1` 是**文件描述符**而不是文件名。如果写成 `2>1`，就会创建一个名为 `1` 的文件。`2>&1` 才是"把 stderr 指向 stdout 的位置"。

---

### 重定向速查表

| 符号 | 作用 | 助记 |
|------|------|------|
| `>` | stdout 写入文件（覆盖） | 一个箭头 = 覆盖 |
| `>>` | stdout 追加到文件 | 两个箭头 = 追加 |
| `2>` | stderr 写入文件 | `2` 是 stderr 的编号 |
| `2>&1` | stderr → stdout 的位置 | `&` 表示"文件描述符" |
| `\|` | 管道，左边的 stdout → 右边的 stdin | 像水管一样连接 |

---

## 3. 后台进程管理

### `python train.py &`

```bash
python train.py &
```

| 部分 | 含义 |
|------|------|
| `python train.py` | 执行训练脚本 |
| `&` | 放在命令末尾，表示在**后台**运行。终端会立即返回提示符，你可以继续输入其他命令 |

**注意：** 输出仍然会打印到终端，容易把你的操作搞得很混乱。而且**关闭终端后进程会被杀掉**。

---

### `nohup python train.py > train.log 2>&1 &`

```bash
nohup python train.py > train.log 2>&1 &
```

这条命令是后台运行的"完整版"，每一段都有作用：

| 部分 | 含义 |
|------|------|
| `nohup` | **No Hang Up**。让命令忽略 `SIGHUP` 信号（关闭终端时系统会发这个信号给所有子进程），使得关闭终端后进程仍然存活 |
| `python train.py` | 你要运行的实际命令 |
| `> train.log` | stdout 写入文件 |
| `2>&1` | stderr 也写入同一个文件 |
| `&` | 放入后台运行 |

**组合效果：** 进程在后台运行，所有输出写入 `train.log`，关闭终端也不会中断。

---

### `jobs` / `ps aux | grep train.py`

```bash
jobs
```

| 部分 | 含义 |
|------|------|
| `jobs` | 列出当前 Shell 会话中的后台任务。只能看到**当前终端**启动的后台进程 |

```bash
ps aux | grep train.py
```

| 部分 | 含义 |
|------|------|
| `ps` | **P**rocess **S**tatus，显示进程列表 |
| `a` | 显示所有用户的进程 |
| `u` | 以用户友好的格式显示 |
| `x` | 包括没有关联到终端的进程 |
| `\| grep train.py` | 从结果中筛选包含 `train.py` 的行 |

---

### `fg %1` / `kill %1`

```bash
fg %1
```

| 部分 | 含义 |
|------|------|
| `fg` | **F**ore**g**round，把后台任务恢复到前台 |
| `%1` | 任务编号 1（`jobs` 命令显示的编号） |

```bash
kill %1
```

| 部分 | 含义 |
|------|------|
| `kill` | 终止进程 |
| `%1` | 指定任务编号。也可以用 PID（进程 ID）来 kill |

```bash
kill $(pgrep -f "train.py")
```

| 部分 | 含义 |
|------|------|
| `pgrep` | **P**rocess **Grep**，搜索匹配模式的进程并返回 PID |
| `-f` | 匹配**完整命令行**（不只是进程名） |
| `"train.py"` | 搜索关键字 |
| `$(...)` | **命令替换**，先执行括号里的命令，把输出结果替换到外层命令中。所以 `kill $(pgrep -f "train.py")` 等于先找到 PID，再 kill 那个 PID |

---

## 4. tmux 终端复用器

### 安装

```bash
# macOS
brew install tmux

# Ubuntu
sudo apt install tmux
```

| 部分 | 含义 |
|------|------|
| `brew install` | macOS 上的 Homebrew 包管理器安装命令 |
| `sudo apt install` | Ubuntu/Debian 的包管理器安装命令。`sudo` 表示以管理员权限运行 |

---

### 基本操作

```bash
tmux new -s training
```

| 部分 | 含义 |
|------|------|
| `tmux new` | 创建一个新的 tmux session |
| `-s training` | 给 session 起名为 `training`（`-s` = session name）。起名方便后续 reattach |

---

### tmux 快捷键（全部以 `Ctrl+B` 为前缀）

tmux 的所有快捷键都需要**先按 `Ctrl+B`，松手后再按第二个键**。`Ctrl+B` 叫做 **prefix key**（前缀键）。

| 操作 | 按键 | 详细说明 |
|------|------|----------|
| 水平分割窗口 | `Ctrl+B` 然后 `"` | 把当前 pane 上下切成两半（`"` 像两条横线，所以是水平分割） |
| 垂直分割窗口 | `Ctrl+B` 然后 `%` | 把当前 pane 左右切成两半（`%` 像有个竖线，所以是垂直分割） |
| 在 pane 间切换 | `Ctrl+B` 然后方向键 | 用 ↑ ↓ ← → 在不同 pane 之间移动光标 |
| 断开 session | `Ctrl+B` 然后 `d` | **d**etach，断开当前 session（session 在后台继续运行！你可以安全关闭终端或断开 SSH） |

---

### 重新连接和管理

```bash
tmux attach -t training
```

| 部分 | 含义 |
|------|------|
| `tmux attach` | 重新连接到一个已存在的 session |
| `-t training` | **t**arget，指定要连接的 session 名称 |

```bash
tmux ls
```

| 部分 | 含义 |
|------|------|
| `tmux ls` | 列出当前所有 tmux session |

```bash
tmux kill-session -t training
```

| 部分 | 含义 |
|------|------|
| `tmux kill-session` | 终止一个 session |
| `-t training` | 指定要终止的 session 名称 |

---

### AI 工作流示例详解

```bash
tmux new -s train
# → 创建并进入名为 "train" 的 session

python train.py --epochs 100 --lr 1e-4
# → 在 Pane 1 中启动训练
#   --epochs 100  : 训练 100 个 epoch
#   --lr 1e-4     : 学习率设为 0.0001

# 按 Ctrl+B, " → 水平分割，出现 Pane 2
watch -n1 nvidia-smi
# → watch 命令：每隔 N 秒重复执行后面的命令
#   -n1 : 每 1 秒执行一次
#   nvidia-smi : NVIDIA GPU 状态查看工具

# 按 Ctrl+B, % → 垂直分割，出现 Pane 3
tail -f logs/experiment.log
# → 实时跟踪日志文件

# 按 Ctrl+B, d → 断开 session
# session 在后台继续运行，训练不会中断
# 随时用 tmux attach -t train 重新连接
```

---

## 5. 系统与 GPU 监控

### `htop`

```bash
htop
```

| 部分 | 含义 |
|------|------|
| `htop` | `top` 命令的增强版，以彩色交互界面显示系统所有进程的 CPU、内存使用情况 |

**htop 界面内操作：**

| 按键 | 作用 | 使用场景 |
|------|------|----------|
| `F6` 或 `>` | 按指定列排序 | 按内存排序，可以发现 memory leak（内存泄漏） |
| `F5` | 切换 tree view（树状视图） | 查看哪个进程派生了哪些子进程 |
| `F9` | Kill 选中的进程 | 直接在界面里终止进程 |
| `/` | 按名字搜索进程 | 快速找到特定进程 |
| `q` | 退出 htop | — |

---

### `nvtop`

```bash
# 安装
sudo apt install nvtop   # Ubuntu
brew install nvtop        # macOS

# 运行
nvtop
```

| 部分 | 含义 |
|------|------|
| `nvtop` | **NV**IDIA **top**，专门监控 NVIDIA GPU 的交互式工具，类似 htop 但针对 GPU |

---

### `nvidia-smi`

```bash
nvidia-smi
```

| 部分 | 含义 |
|------|------|
| `nvidia-smi` | **NVIDIA S**ystem **M**anagement **I**nterface。显示 GPU 状态的快照：温度、显存使用、GPU 利用率、正在使用 GPU 的进程 |

```bash
watch -n1 nvidia-smi
```

| 部分 | 含义 |
|------|------|
| `watch` | 反复执行后面的命令，并刷新显示 |
| `-n1` | 每 **1** 秒刷新一次 |
| `nvidia-smi` | 被反复执行的命令 |

```bash
nvidia-smi --query-compute-apps=pid,name,used_memory --format=csv
```

| 部分 | 含义 |
|------|------|
| `--query-compute-apps=` | 查询正在使用 GPU 的计算进程 |
| `pid,name,used_memory` | 要查询的字段：进程 ID、进程名、使用的显存 |
| `--format=csv` | 输出格式为 CSV（逗号分隔），方便进一步处理 |

---

## 6. SSH 与文件传输

### 基本连接

```bash
ssh user@gpu-box-ip
```

| 部分 | 含义 |
|------|------|
| `ssh` | **S**ecure **Sh**ell，通过加密连接登录远程机器 |
| `user` | 远程机器上的用户名 |
| `@` | 分隔用户名和主机地址 |
| `gpu-box-ip` | 远程机器的 IP 地址或域名 |

```bash
ssh -i ~/.ssh/my_gpu_key user@gpu-box-ip
```

| 部分 | 含义 |
|------|------|
| `-i` | **i**dentity file，指定要使用的私钥文件 |
| `~/.ssh/my_gpu_key` | 私钥文件路径。SSH 使用**密钥对认证**，比密码更安全 |

---

### `scp` — 远程复制文件

```bash
scp model.pt user@gpu-box-ip:~/models/
```

| 部分 | 含义 |
|------|------|
| `scp` | **S**ecure **C**o**p**y，基于 SSH 的加密文件复制 |
| `model.pt` | 本地文件 |
| `user@gpu-box-ip:~/models/` | 远程目标路径。`:` 后面是远程机器上的路径 |

```bash
scp user@gpu-box-ip:~/results/metrics.json ./
```

| 部分 | 含义 |
|------|------|
| `user@gpu-box-ip:~/results/metrics.json` | 远程文件路径（**源**） |
| `./` | 本地当前目录（**目标**） |

> **方向判断：** `scp` 的参数顺序就是 `源 → 目标`。谁带 `user@host:` 前缀，谁就是远程端。

---

### `rsync` — 高效同步目录

```bash
rsync -avz ./data/ user@gpu-box-ip:~/data/
```

| 部分 | 含义 |
|------|------|
| `rsync` | **R**emote **sync**，智能文件同步工具。只传输**有差异的部分**，比 `scp` 快得多 |
| `-a` | **a**rchive 模式：保留权限、时间戳、符号链接等，递归复制子目录 |
| `-v` | **v**erbose，显示详细过程 |
| `-z` | 传输时**压缩**数据，节省带宽 |
| `./data/` | 本地源目录。**注意末尾的 `/`**：有 `/` 表示同步目录里的内容；没有 `/` 表示把整个目录（包括目录本身）复制过去 |
| `user@gpu-box-ip:~/data/` | 远程目标路径 |

> **`rsync` vs `scp` 的区别：**
> - `scp` 每次都完整复制所有文件
> - `rsync` 只传输修改过的文件，适合反复同步大目录

---

### SSH 端口转发

```bash
ssh -L 8888:localhost:8888 user@gpu-box-ip
```

| 部分 | 含义 |
|------|------|
| `-L` | **L**ocal 端口转发 |
| `8888:localhost:8888` | 格式是 `本地端口:目标主机:目标端口`。意思是：把本地的 `8888` 端口转发到远程机器的 `localhost:8888` |
| `user@gpu-box-ip` | 远程机器 |

**效果：** 连接后，在本地浏览器打开 `http://localhost:8888`，就能访问远程机器上跑的 Jupyter Notebook 或 TensorBoard。

---

### SSH Config 文件

在 `~/.ssh/config` 中添加配置，避免每次输入一长串参数：

```text
Host gpu
    HostName 192.168.1.100
    User ubuntu
    IdentityFile ~/.ssh/gpu_key
```

| 字段 | 含义 |
|------|------|
| `Host gpu` | 给这个连接起个别名叫 `gpu` |
| `HostName` | 实际的 IP 地址或域名 |
| `User` | 登录用的用户名 |
| `IdentityFile` | 使用的私钥文件路径 |

**配置后：** `ssh gpu` 就等同于 `ssh -i ~/.ssh/gpu_key ubuntu@192.168.1.100`。

---

## 7. AI 工作常用 Aliases

### 什么是 Alias？

Alias（别名）就是给一串长命令起个短名字。定义在 `~/.zshrc` 或 `~/.bashrc` 中，每次打开终端自动生效。

```bash
source phases/00-setup-and-tooling/10-terminal-and-shell/code/shell_aliases.sh
```

| 部分 | 含义 |
|------|------|
| `source` | 在**当前 Shell** 中执行文件里的命令（和直接运行脚本不同，`source` 不会创建子进程，所以定义的变量和 alias 会在当前终端生效） |

---

### 常用 Alias 逐条解释

```bash
alias gpu='nvidia-smi --query-gpu=index,name,utilization.gpu,memory.used,memory.total,temperature.gpu --format=csv,noheader'
```

| 部分 | 含义 |
|------|------|
| `alias gpu='...'` | 定义别名 `gpu`，之后输入 `gpu` 就会执行引号里的命令 |
| `--query-gpu=` | 查询 GPU 信息 |
| `index` | GPU 编号（多卡时区分第 0 张、第 1 张等） |
| `name` | GPU 型号名 |
| `utilization.gpu` | GPU 计算利用率（百分比） |
| `memory.used` / `memory.total` | 已用显存 / 总显存 |
| `temperature.gpu` | GPU 温度 |
| `--format=csv,noheader` | 输出 CSV 格式，不带表头 |

```bash
alias killtraining='pkill -f "python.*train"'
```

| 部分 | 含义 |
|------|------|
| `pkill` | **P**rocess **kill**，按模式匹配并终止进程 |
| `-f` | 匹配**完整命令行** |
| `"python.*train"` | 正则表达式：匹配包含 `python` 后面跟着 `train` 的任何进程 |

```bash
alias ae='source .venv/bin/activate'
```

| 部分 | 含义 |
|------|------|
| `ae` | **a**ctivate **e**nvironment 的缩写 |
| `source .venv/bin/activate` | 激活当前目录下的 Python 虚拟环境 |

```bash
alias watchloss='tail -f logs/*.log | grep --line-buffered "loss"'
```

| 部分 | 含义 |
|------|------|
| `tail -f logs/*.log` | 实时跟踪 `logs/` 下所有日志文件 |
| `grep --line-buffered "loss"` | 只显示包含 `"loss"` 的行，实时输出 |

---

## 8. 常见 AI 终端模式

### 训练 + 记录日志 + 完成后通知

```bash
python train.py 2>&1 | tee train.log; echo "DONE" | mail -s "Training complete" you@email.com
```

| 部分 | 含义 |
|------|------|
| `python train.py 2>&1` | 运行训练，把 stderr 合并到 stdout |
| `\| tee train.log` | `tee` 命令：**同时**把输出写入文件和显示在屏幕上。像 T 型管道，一路走两个方向 |
| `;` | 前一条命令执行完后，执行下一条（不管前面是否成功） |
| `echo "DONE" \| mail -s "Training complete" you@email.com` | 训练结束后发邮件通知。`-s` 是邮件主题（subject） |

---

### 比较两个实验的结果

```bash
diff <(grep "accuracy" exp1.log) <(grep "accuracy" exp2.log)
```

| 部分 | 含义 |
|------|------|
| `diff` | 比较两个输入的差异 |
| `<(...)` | **进程替换**（Process Substitution）。把括号里命令的输出**当作一个临时文件**传给 `diff`。这样就不需要先把 grep 结果存成文件再比较 |
| `grep "accuracy" exp1.log` | 从实验 1 的日志中提取含 `accuracy` 的行 |
| `grep "accuracy" exp2.log` | 从实验 2 的日志中提取含 `accuracy` 的行 |

---

### 找最大的模型文件

```bash
find . -name "*.pt" -o -name "*.safetensors" | xargs du -h | sort -rh | head -20
```

| 部分 | 含义 |
|------|------|
| `find .` | 从当前目录开始递归搜索 |
| `-name "*.pt"` | 匹配 `.pt` 文件（PyTorch 模型） |
| `-o` | **Or**（或），连接多个条件 |
| `-name "*.safetensors"` | 匹配 `.safetensors` 文件 |
| `\| xargs du -h` | `xargs` 把前面的输出（文件名列表）作为参数传给 `du -h`。`du` = **D**isk **U**sage，`-h` = **h**uman-readable（显示 KB/MB/GB） |
| `\| sort -rh` | 按大小**逆序**（`-r`）、**人类可读数字**（`-h`，理解 K/M/G）排序 |
| `\| head -20` | 只显示前 20 行（最大的 20 个文件） |

---

### 下载模型 / 解压数据集

```bash
wget https://huggingface.co/model/resolve/main/model.safetensors
```

| 部分 | 含义 |
|------|------|
| `wget` | **W**eb **Get**，从 URL 下载文件到当前目录 |

```bash
tar xzf dataset.tar.gz -C ./data/
```

| 部分 | 含义 |
|------|------|
| `tar` | **T**ape **Ar**chive，打包/解包工具 |
| `x` | e**x**tract，解压 |
| `z` | 通过 g**z**ip 解压（处理 `.gz` 压缩） |
| `f` | 后面跟**文件名** |
| `dataset.tar.gz` | 要解压的文件 |
| `-C ./data/` | 解压到 `./data/` 目录（**C**hange directory） |

> **助记：** `tar xzf` = "e**x**tract g**z**ip **f**ile"

---

### 统计代码行数

```bash
find . -name "*.py" | xargs wc -l | tail -1
```

| 部分 | 含义 |
|------|------|
| `find . -name "*.py"` | 找到所有 Python 文件 |
| `\| xargs wc -l` | 统计每个文件的行数 |
| `\| tail -1` | 只取最后一行，即**总计**行数（`wc` 处理多个文件时会在最后一行输出 `total`） |

---

### 磁盘空间检查

```bash
df -h
```

| 部分 | 含义 |
|------|------|
| `df` | **D**isk **F**ree，显示文件系统的磁盘空间使用情况 |
| `-h` | **h**uman-readable，以 GB/MB 等单位显示 |

```bash
du -sh ./data/*
```

| 部分 | 含义 |
|------|------|
| `du` | **D**isk **U**sage，显示文件/目录占用的空间 |
| `-s` | **s**ummarize，只显示总计而不列出子目录 |
| `-h` | **h**uman-readable |
| `./data/*` | `data/` 目录下的每个文件和子目录 |

---

### 检查环境变量

```bash
env | grep -i cuda
env | grep -i torch
```

| 部分 | 含义 |
|------|------|
| `env` | 列出当前所有环境变量 |
| `\| grep -i cuda` | 筛选包含 `cuda` 的行。`-i` = case-**i**nsensitive（不区分大小写），所以 `CUDA`、`cuda`、`Cuda` 都能匹配 |

**常见用途：** 训练前确认 `CUDA_VISIBLE_DEVICES`、`CUDA_HOME` 等变量是否正确设置。

---

## 练习命令详解

课程中的第 3 题练习包含一条较复杂的命令，这里拆开来看：

```bash
for i in $(seq 1 100); do echo "epoch $i loss: $(echo "scale=4; 1/$i" | bc)"; sleep 0.1; done > fake_train.log
```

| 部分 | 含义 |
|------|------|
| `for i in $(seq 1 100)` | 循环变量 `i` 从 1 到 100。`seq 1 100` 生成数字序列 |
| `do ... done` | 循环体 |
| `echo "epoch $i loss: ..."` | 打印每个 epoch 的模拟日志 |
| `$(echo "scale=4; 1/$i" \| bc)` | `bc` 是计算器程序。`scale=4` 设置小数位数为 4。`1/$i` 计算 1/i 的值。整体效果是生成递减的 loss 值 |
| `sleep 0.1` | 暂停 0.1 秒，模拟真实训练的时间间隔 |
| `> fake_train.log` | 整个循环的输出写入文件 |

---

> 💡 **学习建议：** 不用死记硬背每条命令。多在终端中实际敲一敲，遇到不懂的参数就用 `man <命令>` 或 `<命令> --help` 查看帮助文档。用多了自然就记住了。
