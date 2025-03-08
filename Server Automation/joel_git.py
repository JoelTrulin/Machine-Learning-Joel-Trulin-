import os
import time
import subprocess

Project = 'my-byte'
Folder_name ='Joel'
git_user_name = 'JoelTrulin-capestart'
git_user_email = 'joel.trulin@capestart.com'
branch = 'face_id'
token = ''


repo_url = f'https://{git_user_name}:{token}@github.com/capestart/MyByte-Face_ID_Screening.git'
path = f'{Project}/{Folder_name}/{repo_url[:-4].split("/")[-1]}'

clone_command = f'git clone {repo_url} {path} -b {branch}'
# Execute the Git clone command
os.system(clone_command)

cwd = os.getcwd()
os.chdir(path)
# Set user name and email
os.system(f'git config --local user.name "{git_user_name}"')
os.system(f'git config --local user.email "{git_user_email}"')
os.chdir(cwd)

branch2 = 'Llama'
repo_url2 = f'https://{git_user_name}:{token}@github.com/JoelTrulin-capestart/Resource-Monitor.git'
path2 = f'{Project}/{Folder_name}/{repo_url2[:-4].split("/")[-1]}'
clone_command2 = f'git clone {repo_url2} {path2} -b {branch2}'
os.system(clone_command2)

cwd = os.getcwd()
os.chdir(path2)
# Set user name and email
os.system(f'git config --local user.name "{git_user_name}"')
os.system(f'git config --local user.email "{git_user_email}"')
os.chdir(cwd)