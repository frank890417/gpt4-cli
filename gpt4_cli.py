import argparse
import openai
import os
from dotenv import load_dotenv

# 载入.env文件中的变量
load_dotenv()

def generate_gpt4_response(prompt, language):
    openai.api_key = os.environ["OPENAI_API_KEY"]

    engine = "text-davinci-002"
    if language == 'zh':
        engine = "text-davinci-002-zh"

    response = openai.Completion.create(
        engine=engine,
        prompt=prompt,
        temperature=0.5,
        max_tokens=50,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    return response.choices[0].text.strip()

def should_execute(prompt):
    while True:
        answer = input(f"The translated command is:\n{prompt}\nDo you want to execute it? [Y/n]: ").strip().lower()
        if answer == "" or answer == "y" or answer == "yes":
            return True
        elif answer == "n" or answer == "no":
            return False
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

def main(language):
    print("Enter 'q' or 'quit' to exit the interactive mode.")
    while True:
        nl_command = input("> ")

        if nl_command.lower() in ["q", "quit"]:
            break

        if language == "zh":
            prompt = f"将以下自然语言命令翻译成Linux命令：{nl_command}"
        else:
            prompt = f"Translate the following natural language command to a Linux command: {nl_command}"

        linux_command = generate_gpt4_response(prompt, language)

        if should_execute(linux_command):
            # 执行获取的Linux指令
            os.system(linux_command)
        else:
            print("Command not executed.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Command line utility to interact with GPT-4 using natural language.")
    parser.add_argument("-l", "--language", type=str, default="en", help="The input language for natural language commands. Supported languages: en (English), zh (Simplified Chinese). Default is en.")
    args = parser.parse_args()

    if args.language not in ["en", "zh"]:
        print("Error: Invalid language. Supported languages are 'en' (English) and 'zh' (Simplified Chinese).")
    else:
        main(args.language)
