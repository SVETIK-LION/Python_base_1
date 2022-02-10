import os


def make_dir(name_dir='my_dir', name_base_dir='my_project'):
    BASE_DIR_PATH = os.path.dirname(os.path.abspath(__file__))
    name_base_dir_path = os.path.join(BASE_DIR_PATH, f'{name_base_dir}')
    if not os.path.exists(name_base_dir):
        os.mkdir(name_base_dir)
    else:
        print(f'Дириктория с именем {name_base_dir} уже существует, она не будет добавлена')

    name_dir_path = os.path.join(name_base_dir_path, f'{name_dir}')
    if not os.path.exists(name_dir_path):
        os.mkdir(name_dir_path)
    else:
        print(f'Дириктория с именем {name_dir} уже существует, она не будет добавлена')


make_dir('settings')
make_dir('mainapp')
make_dir('adminapp')
make_dir('authapp')
