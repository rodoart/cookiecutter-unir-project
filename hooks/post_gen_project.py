import os
import subprocess
import pathlib

CURRENT_DIR = pathlib.Path(".").resolve()

MESSAGE_COLOR = "\x1b[34m"
RESET_ALL = "\x1b[0m"

print(f"Creating virtual enviroment...{RESET_ALL}")
subprocess.call(['conda', 'env', 'create', '--file', 'environment.yml'])

print(f"Starting virtual envirmoment...{RESET_ALL}")
subprocess.call(['conda', 'activate', '{{ cookiecutter.project_slug }}'])

print(f"Downloading tex template...{RESET_ALL}")
import requests
url = 'https://raw.githubusercontent.com/rodoart/latex-apaarticle-cls/master/apa_article.cls'
r = requests.get(url, allow_redirects=True)
open(DATA_DIR.joinpath("latex", "apa_article.cls"), 'wb').write(r.content)


file_object = open('.gitignore', 'a')
file_object.write('\n/data/')
file_object.close()

print(f"{MESSAGE_COLOR}Almost done!")
print(f"Initializing a git repository...{RESET_ALL}")

subprocess.call(['git', 'init'])
subprocess.call(['git', 'add', '*'])
subprocess.call(['git', 'commit', '-m', 'Initial commit'])



print(f"{MESSAGE_COLOR}The beginning of your destiny is defined now! Create and have fun!{RESET_ALL}")




