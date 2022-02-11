import os
import shutil


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
my_project_path = os.path.join(BASE_DIR, 'my_project')
for root, dirs, files in os.walk(my_project_path):
    for dir in dirs:
        if dir == 'templates':
            shutil.copytree(os.path.join(root, dir), os.path.join(BASE_DIR, 'templates'), dirs_exist_ok=True)
