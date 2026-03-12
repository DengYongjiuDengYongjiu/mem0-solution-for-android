#!/usr/bin/env python3
"""
mem0 API 模式使用示例
无需本地依赖，直接调用 mem0.ai 云服务
"""

import httpx
import json

# 配置
API_KEY = "your-mem0-api-key"  # 替换为你的 API key
API_BASE = "https://api.mem0.ai/v1"

class Mem0Client:
    """mem0 API 客户端"""
    
    def __init__(self, api_key: str):
        self.client = httpx.Client(
            base_url=API_BASE,
            headers={"Authorization": f"Bearer {api_key}"}
        )
    
    def add_memory(self, messages: list, user_id: str) -> dict:
        """添加记忆"""
        response = self.client.post(
            "/memories/",
            json={"messages": messages, "user_id": user_id}
        )
        response.raise_for_status()
        return response.json()
    
    def search_memories(self, query: str, user_id: str, limit: int = 5) -> dict:
        """搜索记忆"""
        response = self.client.post(
            "/search/",
            json={"query": query, "user_id": user_id, "limit": limit}
        )
        response.raise_for_status()
        return response.json()
    
    def get_all_memories(self, user_id: str) -> dict:
        """获取用户所有记忆"""
        response = self.client.get(f"/memories/{user_id}")
        response.raise_for_status()
        return response.json()
    
    def delete_memory(self, memory_id: str) -> dict:
        """删除记忆"""
        response = self.client.delete(f"/memories/{memory_id}")
        response.raise_for_status()
        return response.json()


# ============ 使用示例 ============

if __name__ == "__main__":
    # 初始化客户端
    client = Mem0Client(api_key=API_KEY)
    
    print("=" * 50)
    print("mem0 API 使用示例")
    print("=" * 50)
    
    # 示例 1: 添加记忆
    print("\n1️⃣ 添加记忆")
    messages = [
        {"role": "user", "content": "我喜欢喝咖啡，不喜欢茶"},
        {"role": "assistant", "content": "好的，我记住了你喜欢咖啡"}
    ]
    try:
        result = client.add_memory(messages, user_id="user_001")
        print(f"✅ 添加成功：{json.dumps(result, indent=2)}")
    except Exception as e:
        print(f"❌ 错误：{e}")
    
    # 示例 2: 搜索记忆
    print("\n2️⃣ 搜索记忆")
    try:
        results = client.search_memories("用户喜欢喝什么？", user_id="user_001")
        print(f"🔍 搜索结果：{json.dumps(results, indent=2, ensure_ascii=False)}")
    except Exception as e:
        print(f"❌ 错误：{e}")
    
    # 示例 3: 获取所有记忆
    print("\n3️⃣ 获取所有记忆")
    try:
        memories = client.get_all_memories("user_001")
        print(f"📋 记忆列表：{json.dumps(memories, indent=2, ensure_ascii=False)}")
    except Exception as e:
        print(f"❌ 错误：{e}")
