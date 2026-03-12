#!/data/data/com.termux/files/usr/bin/bash
# mem0 环境快速恢复脚本 - for Android/Termux
# 用法：./restore.sh

set -e

echo "=========================================="
echo "  mem0 环境快速恢复 - for Android/Termux"
echo "=========================================="
echo ""

# 检查 Termux
if [ ! -d "/data/data/com.termux" ]; then
    echo "❌ 错误：请在 Termux 中运行此脚本"
    exit 1
fi

# 检查 mamba
if ! command -v mamba &> /dev/null; then
    echo "⚠️  mamba 未安装，正在安装..."
    curl -Ls https://micro.mamba.pm/install.sh | sh
    source ~/.bashrc
fi

# 检查环境文件
ENV_FILE="mem0-env.tar.gz"
if [ ! -f "$ENV_FILE" ]; then
    echo "⚠️  预编译环境文件不存在"
    echo ""
    echo "请从 GitHub Release 下载:"
    echo "https://github.com/DengYongjiuDengYongjiu/mem0-solution-for-android/releases/tag/v1.0.0"
    echo ""
    echo "或使用 wget 下载:"
    echo "wget https://github.com/DengYongjiuDengYongjiu/mem0-solution-for-android/releases/download/v1.0.0/mem0-env.tar.gz"
    echo ""
    exit 1
fi

# 创建目录
echo "📁 创建环境目录..."
mkdir -p ~/.local/share/mamba/envs/

# 检查是否已存在
if [ -d "~/.local/share/mamba/envs/mem0" ]; then
    echo "⚠️  mem0 环境已存在"
    read -p "是否覆盖？(y/N): " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        echo "❌ 取消恢复"
        exit 1
    fi
    rm -rf ~/.local/share/mamba/envs/mem0
fi

# 解压环境
echo "📦 解压预编译环境 (这可能需要 1-2 分钟)..."
tar -xzf "$ENV_FILE" -C ~/.local/share/mamba/envs/

# 验证
if [ -d "~/.local/share/mamba/envs/mem0" ]; then
    echo "✅ 环境解压成功"
else
    echo "❌ 环境解压失败"
    exit 1
fi

# 测试激活
echo "🧪 测试环境..."
source ~/.local/share/mamba/envs/mem0/bin/activate
if command -v python &> /dev/null; then
    PYTHON_VERSION=$(python --version 2>&1)
    echo "✅ Python 版本：$PYTHON_VERSION"
    
    # 检查 mem0
    if python -c "import mem0" 2>/dev/null; then
        MEM0_VERSION=$(python -c "import mem0; print(mem0.__version__)" 2>/dev/null || echo "unknown")
        echo "✅ mem0 版本：$MEM0_VERSION"
    else
        echo "⚠️  mem0 导入失败，请检查环境"
    fi
else
    echo "❌ Python 不可用"
    exit 1
fi

echo ""
echo "=========================================="
echo "  ✅ 恢复完成!"
echo "=========================================="
echo ""
echo "使用方法:"
echo "  mamba activate mem0"
echo "  python examples/test_mem0.py"
echo ""
echo "或查看示例代码:"
echo "  ls examples/"
echo ""
