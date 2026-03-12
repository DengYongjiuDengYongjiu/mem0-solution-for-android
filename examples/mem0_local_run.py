#!/usr/bin/env python3
"""
mem0 本地模式运行示例
使用：Qdrant (本地) + Ollama (本地) 或 OpenAI 兼容 API
"""

import json

print("=" * 60)
print("mem0 本地模式")
print("=" * 60)

# 配置
config = {
    "vector_store": {
        "provider": "qdrant",
        "config": {
            "host": "localhost",
            "port": 6333,
            "path": "/data/data/app.botdrop/files/home/qdrant_data"
        }
    },
    # 使用 OpenAI 兼容 API（可以用 Ollama 替代）
    "llm": {
        "provider": "openai",
        "config": {
            "model": "gpt-3.5-turbo",
            "api_key": "sk-test"  # 占位符
        }
    },
    "embedder": {
        "provider": "openai",
        "config": {
            "model": "text-embedding-ada-002",
            "api_key": "sk-test"  # 占位符
        }
    }
}

try:
    from mem0 import Memory
    
    print("\n📋 配置:")
    print(json.dumps(config, indent=2))
    
    print("\n🔧 初始化 Memory...")
    memory = Memory.from_config(config)
    print("✅ Memory 初始化成功!")
    
    print("\n💾 添加测试记忆...")
    messages = [
        {"role": "user", "content": "我喜欢喝咖啡，不喜欢茶"},
        {"role": "assistant", "content": "好的，我记住了你喜欢咖啡"}
    ]
    result = memory.add(messages, user_id="test_user")
    print(f"✅ 添加成功：{result}")
    
    print("\n🔍 搜索记忆...")
    query = "用户喜欢喝什么？"
    results = memory.search(query, user_id="test_user", limit=3)
    print(f"✅ 搜索结果：")
    for r in results.get('results', []):
        print(f"  - {r.get('memory', 'N/A')} (score: {r.get('score', 0):.2f})")
    
    print("\n🎉 mem0 本地模式运行成功!")
    
except Exception as e:
    print(f"\n⚠️ 配置说明:")
    print(f"   当前配置使用 OpenAI API（需要 API key）")
    print(f"   如需纯本地运行，需要安装 Ollama:")
    print(f"   1. curl -fsSL https://ollama.ai/install.sh | sh")
    print(f"   2. ollama pull llama3.2")
    print(f"   3. ollama pull nomic-embed-text")
    print(f"\n❌ 错误：{e}")
    import traceback
    traceback.print_exc()
