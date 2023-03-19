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

def execute_natural_language_command(nl_command, force_execution, language="en"):
    if language == "zh":
        prompt = f"將以下自然語言命令翻譯成Linux命令：{nl_command}"
    else:
        prompt = f"Translate the following natural language command to a Linux command: {nl_command}"

    linux_command = generate_gpt4_response(prompt, language)

    if force_execution or should_execute(linux_command):
        # Execute the obtained Linux command
        os.system(linux_command)
    else:
        print("Command not executed.")


def main(language):
    if args.interactive:
        print("Enter 'q' or 'quit' to exit the interactive mode.")
        while True:
            nl_command = input("> ")

            if nl_command.lower() in ["q", "quit"]:
                break

            execute_natural_language_command(nl_command, args.force, language)
    else:
        if args.command is not None:
            execute_natural_language_command(args.command, args.force, language)
        else:
            print("Error: No command provided. Use --interactive or --i or provide a command.")

            

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="GPT-4 CLI tool for executing terminal commands with natural language")
    parser.add_argument("command", type=str, nargs="?", help="Natural language command", default=None)
    parser.add_argument("-f", "--force", action="store_true", help="Force execution without confirmation")
    parser.add_argument("-i", "--interactive", action="store_true", help="Enter interactive mode for continuous input")
    parser.add_argument("-l", "--language", type=str, default="en", help="The input language for natural language commands. Supported languages: en (English), zh (Simplified Chinese). Default is en.")

    args = parser.parse_args()

    if args.language not in ["en", "zh"]:
        print("Error: Invalid language. Supported languages are 'en' (English) and 'zh' (Simplified Chinese).")
    else:
        main(args.language)
