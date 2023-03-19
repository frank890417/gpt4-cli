# GPT-4 Command Line Interface

![](demo.png)

## 用自然語言控制你的終端機！神奇的 GPT-4 CLI 工具
在這個科技日新月異的時代，AI 已經成為了我們日常生活中的重要角色。而今天，我們要介紹一款利用 OpenAI 的 GPT-4 技術，讓你用自然語言與終端機互動的神奇工具！
### 緣起
我們都知道，終端機是個功能強大的工具，但對於初學者和非技術專業人士來說，學會使用各種指令可能是個挑戰。想像一下，如果你能直接用自然語言告訴終端機你想做什麼，而不用記住繁瑣的指令該有多好！為了實現這個目標，我們開發了這款名為 GPT-4 CLI 的命令列工具，讓你用自然語言控制 Mac 終端機。
### 功能
GPT-4 CLI 是一個基於 Python 開發的命令列工具。它利用了 OpenAI 的 GPT-4 模型，將你輸入的自然語言轉換成對應的終端機指令。例如，當你想創建一個名為 `test_folder` 的資料夾時，只需輸入：

```
please create a new folder named test_folder

```

GPT-4 CLI 將自動識別你的需求並執行對應的指令，即 `mkdir test_folder`。
### 安裝和使用
安裝 GPT-4 CLI 非常簡單。首先，在終端機中運行以下命令，克隆專案並進入專案資料夾：

```
git clone https://github.com/your_username/gpt4-cli.git
cd gpt4-cli

```

然後，運行 `install.sh` 腳本以自動完成安裝：

```
./install.sh

```

安裝完成後，重新啟動終端機，或運行 `source ~/.bashrc`（或相應的 shell 配置文件）以應用更改。你可以開始使用 `please` 或 `pls` 命令與 GPT-4 CLI 互動了。

為了確保安全性，GPT-4 CLI 會在執行指令前詢問你是否確定要執行，只需按 Enter 確認即可。你還可以使用 `-f` 參數強制執行


***

A simple command line tool for interacting with GPT-4 using natural language.

## Installation

1. Install Python and necessary dependencies:

```bash
pip install openai argparse python-dotenv
```

2. Set up your .env file with your GPT-4 API key:
```
OPENAI_API_KEY=<your_api_key_here>
```

3. Run the install.sh script to automatically set up the command aliases:
```
./install.sh
```

4. Restart your terminal or run 'source ~/.bashrc' (or the respective shell configuration file) to apply the changes.

## Usage
To use the command line tool, type please or pls (case-insensitive) followed by your natural language command:

```
please "create a new folder named test_folder"
```
or

```
Pls "create a new folder named test_folder"
```

By default, the tool will ask for your confirmation before executing the translated command. If you want to force the execution without asking for confirmation, use the -f or --force option:
 
```
Pls --force "create a new folder named test_folder"
```
# gpt4-cli
