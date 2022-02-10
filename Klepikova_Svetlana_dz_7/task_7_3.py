import os
import shutil


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
my_project_path = os.path.join(BASE_DIR, 'my_project')
templates_new_path = os.path.join(my_project_path, 'templates')
for root, dirs, files in os.walk(my_project_path):
    for i in range(len(dirs)):
        if dirs[i] == 'templates':
            shutil.copy2(os.path.join(dirs[i]), os.path.join(BASE_DIR, 'templates'))
