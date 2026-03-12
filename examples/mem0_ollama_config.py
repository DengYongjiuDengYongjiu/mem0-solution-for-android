#!/usr/bin/env python3
"""
mem0 纯本地模式配置 (Ollama + Qdrant)
"""

import os

print("=" * 60)
print("mem0 纯本地模式配置")
print("=" * 60)

# 检查服务
import subprocess

# 检查 Ollama
try:
    result = subprocess.run(
        ["/data/data/app.botdrop/files/home/ollama/bin/ollama", "list"],
        capture_output=True, text=True, timeout=30,
        env={**os.environ, "LD_LIBRARY_PATH": "/data/data/app.botdrop/files/usr/lib:/system/lib64"}
    )
    print(f"\n✅ Ollama 已安装")
    print(result.stdout)
except Exception as e:
    print(f"\n⚠️ Ollama: {e}")

# 检查 Qdrant
import urllib.request
try:
    with urllib.request.urlopen("http://localhost:6333/", timeout=5) as resp:
        print(f"✅ Qdrant 已运行 (localhost:6333)")
except Exception as e:
    print(f"⚠️ Qdrant: {e}")

print("\n" + "=" * 60)
print("配置代码:")
print("=" * 60)
print("""
from mem0 import Memory

config = {
    "llm": {
        "provider": "ollama",
        "config": {
            "model": "phi3.5",
            "base_url": "http://localhost:11434"
        }
    },
    "embedder": {
        "provider": "ollama",
        "config": {
            "model": "nomic-embed-text",
            "base_url": "http://localhost:11434"
        }
    },
    "vector_store": {
        "provider": "qdrant",
        "config": {
            "host": "localhost",
            "port": 6333
        }
    }
}

memory = Memory.from_config(config)

# 添加记忆
memory.add(
    [{"role": "user", "content": "我喜欢 Python"}],
    user_id="user123"
)

# 搜索记忆
results = memory.search("用户喜欢什么？", user_id="user123")
print(results)
""")

print("\n📋 下一步:")
print("1. 下载模型：/data/data/app.botdrop/files/home/ollama/bin/ollama pull phi3.5")
print("2. 下载嵌入模型：/data/data/app.botdrop/files/home/ollama/bin/ollama pull nomic-embed-text")
print("3. 运行上面的 Python 代码")
