#!/usr/bin/env python3
from mem0 import Memory

print("=" * 50)
print("mem0 本地模式测试")
print("=" * 50)

# 初始化 Memory（本地模式）
try:
    memory = Memory()
    print("✅ Memory 初始化成功")
    
    # 添加记忆
    messages = [
        {"role": "user", "content": "我喜欢喝咖啡"},
        {"role": "assistant", "content": "好的，记住了"}
    ]
    result = memory.add(messages, user_id="test_user")
    print(f"✅ 添加记忆成功：{result}")
    
    # 搜索记忆
    results = memory.search("用户喜欢什么？", user_id="test_user")
    print(f"✅ 搜索记忆成功：{results}")
    
    print("\n🎉 mem0 本地模式完全可用!")
    
except Exception as e:
    print(f"❌ 错误：{e}")
    import traceback
    traceback.print_exc()
