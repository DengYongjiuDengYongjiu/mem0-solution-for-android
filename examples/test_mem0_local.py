#!/usr/bin/env python3
from mem0 import Memory
from mem0.configs.base import MemoryConfig

print("=" * 50)
print("mem0 本地模式测试")
print("=" * 50)

# 配置本地模式（使用 Ollama 或其他本地 LLM）
config = MemoryConfig(
    llm={
        "provider": "ollama",
        "config": {
            "model": "llama3.2",
            "base_url": "http://localhost:11434"
        }
    },
    embedder={
        "provider": "ollama",
        "config": {
            "model": "nomic-embed-text",
            "base_url": "http://localhost:11434"
        }
    },
    vector_store={
        "provider": "qdrant",
        "config": {
            "host": "localhost",
            "port": 6333,
            "path": "./qdrant_data"  # 本地存储
        }
    }
)

try:
    memory = Memory.from_config(config)
    print("✅ Memory 初始化成功（本地模式）")
    
    # 添加记忆
    messages = [
        {"role": "user", "content": "我喜欢喝咖啡"},
        {"role": "assistant", "content": "好的，记住了"}
    ]
    result = memory.add(messages, user_id="test_user")
    print(f"✅ 添加记忆成功")
    
    # 搜索记忆
    results = memory.search("用户喜欢什么？", user_id="test_user")
    print(f"✅ 搜索记忆成功")
    
    print("\n🎉 mem0 本地模式完全可用!")
    
except Exception as e:
    print(f"⚠️ 本地模式需要额外配置:")
    print(f"   - Ollama 服务 (http://localhost:11434)")
    print(f"   - Qdrant 向量数据库 (localhost:6333)")
    print(f"\n错误：{e}")
    print("\n💡 或者使用 API 模式:")
    print("   from mem0 import Memory")
    print("   memory = Memory(api_key='your-mem0-api-key')")
