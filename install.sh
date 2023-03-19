#!/bin/bash

# 检查pip是否已经安装
if ! command -v pip &> /dev/null
then
    echo "pip not found. Please install pip and try again."
    exit 1
fi

# 安装必要的Python依赖
pip install openai argparse python-dotenv

# 将gpt4_cli.py设置为可执行
chmod +x gpt4_cli.py

# 获取gpt4_cli.py的绝对路径
SCRIPT_PATH="$(cd "$(dirname "${BASH_SOURCE[0]}")" &> /dev/null && pwd)/gpt4_cli.py"

# 为当前shell添加PATH和别名
export PATH="$PATH:$(dirname "${SCRIPT_PATH}")"
alias Please="python3 ${SCRIPT_PATH}"
alias please="python3 ${SCRIPT_PATH}"
alias Pls="python3 ${SCRIPT_PATH}"
alias pls="python3 ${SCRIPT_PATH}"

# 将PATH和别名添加到shell配置文件
SHELL_CONFIG=""
if [ -f "${HOME}/.bashrc" ]; then
    SHELL_CONFIG="${HOME}/.bashrc"
elif [ -f "${HOME}/.zshrc" ]; then
    SHELL_CONFIG="${HOME}/.zshrc"
elif [ -f "${HOME}/.bash_profile" ]; then
    SHELL_CONFIG="${HOME}/.bash_profile"
else
    echo "Error: Could not find a shell configuration file (.bashrc, .zshrc, or .bash_profile)."
    exit 1
fi

echo "export PATH=\"\$PATH:$(dirname "${SCRIPT_PATH}")\"" >> "${SHELL_CONFIG}"
echo "alias Please=\"python3 ${SCRIPT_PATH}\"" >> "${SHELL_CONFIG}"
echo "alias please=\"python3 ${SCRIPT_PATH}\"" >> "${SHELL_CONFIG}"
echo "alias Pls=\"python3 ${SCRIPT_PATH}\"" >> "${SHELL_CONFIG}"
echo "alias pls=\"python3 ${SCRIPT_PATH}\"" >> "${SHELL_CONFIG}"

echo "Installation complete. Please restart your terminal or run 'source ${SHELL_CONFIG}' to start using 'please' and 'pls' commands."
