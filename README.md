# mem0 本地化解决方案 - for Android/Termux

> 🚀 **预编译环境备份** - 5 分钟快速部署到新设备，无需编译等待！

## 📥 下载地址

**GitHub Release:** https://github.com/DengYongjiuDengYongjiu/mem0-solution-for-android/releases/tag/v1.0.0

**预编译环境:** [mem0-env.tar.gz](https://github.com/DengYongjiuDengYongjiu/mem0-solution-for-android/releases/download/v1.0.0/mem0-env.tar.gz) (141MB, 解压后 509MB)

## 📦 备份内容

```
mem0-solution-for-android/
├── README.md                    # 本说明文档
├── compiled-env/
│   └── mem0-env.tar.gz         # 预编译环境 (76MB, 解压后 509MB)
├── examples/
│   ├── mem0_api_example.py      # API 模式示例
│   ├── mem0_local_fs.py         # 本地文件存储模式
│   ├── mem0_local_run.py        # 本地运行脚本
│   ├── mem0_ollama_config.py    # Ollama 配置示例
│   ├── mem0_usage.py            # 使用指南
│   ├── test_mem0.py             # API 模式测试
│   └── test_mem0_local.py       # 本地模式测试
└── requirements.txt             # 依赖清单 (备用)
```

---

## ⚡ 快速恢复 (推荐)

### 方式 1: 直接恢复预编译环境 (最快 ⭐⭐⭐)

**适用场景:** 新设备/重装系统，5 分钟快速恢复

```bash
# 1. 克隆示例代码
git clone https://github.com/DengYongjiuDengYongjiu/mem0-solution-for-android.git
cd mem0-solution-for-android

# 2. 下载预编译环境 (从 Releases)
mkdir -p ~/.local/share/mamba/envs/
wget https://github.com/DengYongjiuDengYongjiu/mem0-solution-for-android/releases/download/v1.0.0/mem0-env.tar.gz
# 或用浏览器下载后移动到此目录

# 3. 安装 mamba (如果没有)
curl -Ls https://micro.mamba.pm/install.sh | sh
source ~/.bashrc

# 4. 解压预编译环境
tar -xzf mem0-env.tar.gz -C ~/.local/share/mamba/envs/

# 4. 激活环境
mamba activate mem0

# 5. 测试
python examples/test_mem0.py
```

**完成!** 🎉 现在可以开始使用 mem0 了。

---

### 方式 2: 使用 conda-pack 导出 (更灵活)

```bash
# 在源设备上打包
mamba activate mem0
conda-pack -o mem0-packed.tar.gz

# 在新设备上恢复
mkdir -p ~/envs/mem0
tar -xzf mem0-packed.tar.gz -C ~/envs/mem0
source ~/envs/mem0/bin/activate
```

---

### 方式 3: 重新编译 (备用方案)

**适用场景:** 架构不同/备份损坏

```bash
# 1. 安装 Termux 基础工具
pkg update && pkg upgrade
pkg install python rust cmake clang libclang-repl openssl libffi zlib

# 2. 安装 mamba
curl -Ls https://micro.mamba.pm/install.sh | sh
source ~/.bashrc

# 3. 创建环境
mamba create -n mem0 python=3.12 -y
mamba activate mem0

# 4. 安装依赖 (可能需要 20-30 分钟编译)
pip install -r requirements.txt
```

---

## 🔧 环境配置

### API 模式 (最简单)

```bash
# 设置 API Key
export MEM0_API_KEY="your-api-key"

# 运行示例
python examples/mem0_api_example.py
```

### 本地模式

```bash
# 激活环境
mamba activate mem0

# 运行本地模式示例
python examples/mem0_local_fs.py
```

---

## 📱 Termux 环境要求

| 项目 | 要求 | 说明 |
|------|------|------|
| **系统** | Android 10+ | 推荐 Android 12+ |
| **Termux** | 最新版 | 从 F-Droid 下载 |
| **Python** | 3.12 | 包含在预编译环境中 |
| **架构** | aarch64 | ARM64 设备 |
| **存储** | 1GB+ | 环境 509MB + 数据 |

---

## 🗂️ 目录结构说明

### 预编译环境位置

```
~/.local/share/mamba/envs/mem0/
├── bin/          # 可执行文件 (python, pip 等)
├── lib/          # Python 库文件
├── include/      # 头文件
└── conda-meta/   # 包元数据
```

### 数据持久化

```bash
# mem0 数据存储位置
~/.mem0/                    # mem0 配置
~/mem0_data/qdrant/         # Qdrant 向量数据 (如使用本地模式)
```

**建议:** 定期备份 `~/.mem0/` 和 `~/mem0_data/` 目录

---

## 🚀 使用示例

### 1. API 模式

```python
from mem0 import Memory

memory = Memory(api_key="your-api-key")

# 添加记忆
messages = [
    {"role": "user", "content": "我喜欢喝咖啡"}
]
memory.add(messages, user_id="user_001")

# 搜索记忆
results = memory.search("用户喜欢什么？", user_id="user_001")
print(results)
```

### 2. 本地模式

```python
from mem0 import Memory

config = {
    "vector_store": {
        "provider": "qdrant",
        "config": {
            "path": "./mem0_data",
            "on_disk": True
        }
    }
}

memory = Memory.from_config(config)
memory.add([{"role": "user", "content": "测试记忆"}], user_id="test")
```

---

## 🔍 故障排查

### Q: 激活环境失败？

```bash
# 检查环境是否存在
ls ~/.local/share/mamba/envs/mem0/

# 重新解压
tar -xzf compiled-env/mem0-env.tar.gz -C ~/.local/share/mamba/envs/
```

### Q: Python 找不到？

```bash
# 使用完整路径
~/.local/share/mamba/envs/mem0/bin/python examples/test_mem0.py
```

### Q: 权限错误？

```bash
# 修复权限
chmod -R 755 ~/.local/share/mamba/envs/mem0/
```

### Q: 依赖缺失？

```bash
# 重新安装依赖
mamba activate mem0
pip install -r requirements.txt --force-reinstall
```

---

## 📊 性能对比

| 部署方式 | 时间 | 优点 | 缺点 |
|---------|------|------|------|
| **预编译恢复** | 5 分钟 | 快速，无需编译 | 需要下载 76MB |
| **conda-pack** | 10 分钟 | 灵活，可定制 | 需要源环境 |
| **重新编译** | 30 分钟 | 最新依赖 | 耗时，可能失败 |

---

## 🔗 相关资源

- **GitHub:** https://github.com/DengYongjiuDengYongjiu/mem0-termux-solution
- **mem0 官方:** https://docs.mem0.ai/
- **Termux:** https://termux.dev/
- **Mamba:** https://mamba.readthedocs.io/

---

## 📝 更新日志

### v1.0.0 (2026-03-12)
- ✅ 首次发布
- ✅ 包含预编译环境 (mem0ai==1.0.5)
- ✅ 73 个依赖包完整备份
- ✅ 3 种部署模式示例
- ✅ 完整中文文档

---

*最后更新：2026-03-12*  
*适用于：Android 10+ | Termux | aarch64 | Python 3.12*
