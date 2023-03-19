from setuptools import setup

APP = ['gpt4_cli.py']
DATA_FILES = ['.env']
OPTIONS = {
    'argv_emulation': True,
    'packages': ['openai', 'argparse', 'python-dotenv'],
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
