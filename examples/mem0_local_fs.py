#!/usr/bin/env python3
"""
mem0 本地文件系统模式
不需要 Qdrant 或 Ollama，使用本地文件存储
"""

import os
import json

print("=" * 60)
print("mem0 本地文件系统模式")
print("=" * 60)

# 配置 - 使用本地文件存储
config = {
    "vector_store": {
        "provider": "qdrant",
        "config": {
            "path": "/data/data/app.botdrop/files/home/mem0_data/qdrant",
            "on_disk": True
        }
    },
    "llm": {
        "provider": "openai",
        "config": {
            "model": "gpt-3.5-turbo",
            "api_key": "sk-dummy-key-for-test"
        }
    },
    "embedder": {
        "provider": "openai",
        "config": {
            "model": "text-embedding-ada-002",
            "api_key": "sk-dummy-key-for-test"
        }
    }
}

try:
    from mem0 import Memory
    
    print("\n📋 配置：本地文件存储")
    print(f"   数据路径：{config['vector_store']['config']['path']}")
    
    # 创建数据目录
    os.makedirs(config['vector_store']['config']['path'], exist_ok=True)
    
    print("\n🔧 初始化 Memory...")
    memory = Memory.from_config(config)
    print("✅ Memory 初始化成功!")
    
    print("\n💾 添加测试记忆...")
    messages = [
        {"role": "user", "content": "我喜欢喝咖啡，不喜欢茶"},
        {"role": "assistant", "content": "好的，我记住了"}
    ]
    result = memory.add(messages, user_id="test_user")
    print(f"✅ 添加成功")
    
    print("\n🔍 搜索记忆...")
    results = memory.search("用户喜欢喝什么？", user_id="test_user", limit=3)
    print(f"✅ 搜索结果:")
    for r in results.get('results', []):
        print(f"  - {r.get('memory', 'N/A')} (score: {r.get('score', 0):.2f})")
    
    print("\n🎉 mem0 本地模式运行成功!")
    
except Exception as e:
    print(f"\n❌ 错误：{e}")
    import traceback
    traceback.print_exc()
    
    print("\n" + "=" * 60)
    print("💡 使用建议:")
    print("=" * 60)
    print("""
    方式 1: API 模式（最简单）
    ------------------------
    from mem0 import Memory
    memory = Memory(api_key="your-mem0-api-key")
    
    方式 2: 纯本地模式（需要 Ollama）
    -----------------------------
    1. 安装 Ollama: curl -fsSL https://ollama.ai/install.sh | sh
    2. 下载模型：ollama pull llama3.2
    3. 下载嵌入：ollama pull nomic-embed-text
    4. 配置使用 Ollama 作为 LLM 和 Embedder
    
    方式 3: 使用 OpenAI API
    --------------------
    export OPENAI_API_KEY="sk-..."
    from mem0 import Memory
    memory = Memory()
    """)
