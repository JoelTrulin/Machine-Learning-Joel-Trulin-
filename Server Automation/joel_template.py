import os
import subprocess
try:
    import virtualenv
except:
    subprocess.run("pip install virtualenv", shell=True)
    import virtualenv

Project = 'my-byte'
Folder_name ='Joel'
Env_name = 'faceid_venv'

subprocess.run("sudo pip cache purge", shell=True)
subprocess.run(f"mkdir /{Project}/{Folder_name}", shell=True)

venv_path = f"/{Project}/{Folder_name}/{Env_name}"
subprocess.run(f"virtualenv {venv_path}", shell=True)

env = f'/{Project}/{Folder_name}/{Env_name}/bin/python3 -m'
os.system(f'{env} pip install ipykernel')
os.system(f'{env} ipykernel install --user --name {Env_name}')

commands = ["pip install tensorflow[and-cuda]==2.14",
            "pip install dvc[all]",
            "pip install dvclive",
            "pip install nvitop",
            "pip install livelossplot==0.5.5",
            "pip install opencv-contrib-python==4.8.1.78",
            "pip install ray[default]==2.8.1",
            "pip install tflite-runtime==2.14",
            "pip install torch torchvision torchaudio",
            "pip install transformers accelerate langchain langchain-experimental",
            "pip install jupyter ipywidgets"
            ]
for cmd in commands:
    os.system(f'{env} {cmd}')
