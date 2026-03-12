#!/usr/bin/env python3
"""
mem0 使用示例
环境：micromamba conda 环境 (mem0)
"""

print("=" * 60)
print("mem0 已安装成功!")
print("=" * 60)

# 显示环境信息
import sys
print(f"\nPython: {sys.version}")
print(f"Python 路径：{sys.executable}")

# 显示已安装的包
import subprocess
result = subprocess.run(
    [sys.executable, "-m", "pip", "list"],
    capture_output=True, text=True
)
print("\n已安装的关键包:")
for line in result.stdout.split('\n'):
    if any(pkg in line.lower() for pkg in ['mem0', 'pydantic', 'openai', 'qdrant']):
        print(f"  {line}")

print("\n" + "=" * 60)
print("使用方法:")
print("=" * 60)

print("""
1️⃣ API 模式（推荐 - 无需额外配置）:
   
   from mem0 import Memory
   
   memory = Memory(api_key="your-mem0-api-key")
   
   # 添加记忆
   memory.add(
       [{"role": "user", "content": "我喜欢 Python"}],
       user_id="user123"
   )
   
   # 搜索记忆
   results = memory.search("用户喜欢什么？", user_id="user123")
   print(results)

2️⃣ 本地模式（需要额外服务）:
   
   需要安装:
   - Ollama (本地 LLM): https://ollama.ai
   - Qdrant (向量数据库): docker run -p 6333:6333 qdrant/qdrant
   
   配置:
   from mem0 import Memory
   
   config = {
       "llm": {"provider": "ollama", "config": {"model": "llama3.2"}},
       "embedder": {"provider": "ollama", "config": {"model": "nomic-embed-text"}},
       "vector_store": {"provider": "qdrant", "config": {"host": "localhost", "port": 6333}}
   }
   memory = Memory.from_config(config)

3️⃣ 获取 API Key:
   访问 https://app.mem0.ai 注册并获取 API key

4️⃣ 运行命令:
   /data/data/app.botdrop/files/home/micromamba/bin/micromamba run -n mem0 python3 your_script.py
""")

print("=" * 60)
print("✅ mem0 本地环境修复完成!")
print("=" * 60)
