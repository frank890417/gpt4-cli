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


def get_current_directory_structure():
    files_and_folders = os.listdir()
    directories = [d for d in files_and_folders if os.path.isdir(d)]
    files = [f for f in files_and_folders if os.path.isfile(f)]

    directory_structure = f"Directories: {', '.join(directories)}\nFiles: {', '.join(files)}"
    return directory_structure

# 在主函數或需要生成提示的地方
current_directory_structure = get_current_directory_structure()

def execute_natural_language_command(nl_command, force_execution, language="en"):
        
    if language == "zh":
        prompt = f"將以下自然語言命令翻譯成Linux命令，並在多個命令之間使用分號分隔：{nl_command}\n。The following content does not affect the command line behavior. If the command requires file operations, the current directory structure is as follows: \n{current_directory_structure}\n"
    else:
        prompt = f"Translate the following natural language command to a Linux command, using semicolons to separate multiple commands: {nl_command}\n. The following content does not affect the command line behavior. If the command requires file operations, the current directory structure is as follows:\n{current_directory_structure}\n"
    linux_command = generate_gpt4_response(prompt, language)

    if force_execution or should_execute(linux_command):
        if (force_execution):
            print(linux_command)
        # Execute the obtained Linux command
        os.system(linux_command)
    else:
        print("Command not executed.")


def main(language):
    if args.interactive or args.command is None:
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
