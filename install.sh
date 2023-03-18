#!/bin/bash

# 檢查pip是否已經安裝
if ! command -v pip &> /dev/null
then
    echo "pip not found. Please install pip and try again."
    exit 1
fi

# 安裝必要的Python依賴
pip install openai argparse python-dotenv

# 將gpt4_cli.py設置為可執行
chmod +x gpt4_cli.py

# 獲取gpt4_cli.py的絕對路徑
SCRIPT_PATH="$(cd "$(dirname "${BASH_SOURCE[0]}")" &> /dev/null && pwd)/gpt4_cli.py"

# 為當前shell添加PATH和別名
export PATH="$PATH:$(dirname "${SCRIPT_PATH}")"
alias Please="python ${SCRIPT_PATH}"
alias please="python ${SCRIPT_PATH}"
alias Pls="python ${SCRIPT_PATH}"
alias pls="python ${SCRIPT_PATH}"

# 將PATH和別名添加到shell配置文件
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
echo "alias Please=\"python ${SCRIPT_PATH}\"" >> "${SHELL_CONFIG}"
echo "alias please=\"python ${SCRIPT_PATH}\"" >> "${SHELL_CONFIG}"
echo "alias Pls=\"python ${SCRIPT_PATH}\"" >> "${SHELL_CONFIG}"
echo "alias pls=\"python ${SCRIPT_PATH}\"" >> "${SHELL_CONFIG}"

echo "Installation complete. Please restart your terminal or run 'source ${SHELL_CONFIG}' to start using 'please' and 'pls' commands."
