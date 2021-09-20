import os
import subprocess
import pathlib

CURRENT_DIR = pathlib.Path(".").resolve()

MESSAGE_COLOR = "\x1b[34m"
RESET_ALL = "\x1b[0m"

print(f"Downloading tex template...{RESET_ALL}")
import requests
url = 'https://raw.githubusercontent.com/rodoart/latex-apaarticle-cls/master/apa_article.cls'
r = requests.get(url, allow_redirects=True)
open(CURRENT_DIR.joinpath("latex", "apa_article.cls"), 'wb').write(r.content)

url = 'https://i.ibb.co/C9HY1K6/logo.png'
r = requests.get(url, allow_redirects=True)
open(CURRENT_DIR.joinpath("figures", "logo.png"), 'wb').write(r.content)

print(f"Creating .gitignore file...{RESET_ALL}")

file_object = open('.gitignore', 'a')
file_object.write('\n/data/')
file_object.write('\n/figures/')
file_object.close()

print(f"Creating virtual enviroment...{RESET_ALL}")

enviro_path = CURRENT_DIR.joinpath("python", "environment.yml")
print(f'"{enviro_path}"')

#subprocess.call(['conda', 'env', 'create', '--file', f'"{enviro_path}"'])

os.system(f'conda env create --file "{enviro_path}"')

print(f"Starting virtual envirmoment...{RESET_ALL}")
os.system('conda activate {{ cookiecutter.project_slug }}')

print(f"{MESSAGE_COLOR}Almost done!")
print(f"Initializing a git repository...{RESET_ALL}")

subprocess.call(['git', 'init'])
subprocess.call(['git', 'add', '*'])
subprocess.call(['git', 'commit', '-m', 'Initial commit'])



print(f"{MESSAGE_COLOR}The beginning of your destiny is defined now! Create and have fun!{RESET_ALL}")




