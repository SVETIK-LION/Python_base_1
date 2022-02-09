import os


name_base_dir = 'my_project' # имя внешней папки, которую нужно создать (в данном случае my_project)
BASE_DIR_PATH = os.path.dirname(os.path.abspath(__file__)) # путь до директории, в которой будем создавать папку (где лежит наш скрипт)
name_base_dir_path = os.path.join(BASE_DIR_PATH, f'{name_base_dir}') # создаем путь до новой внешней папки ( у нас my_project)
if not os.path.exists(name_base_dir):
    os.mkdir(name_base_dir) # если по этому пути нет папки с таким названием, то создаем ее
else:
    print(f'Дириктория с именем {name_base_dir} уже существует, введите другое имя')


# функция, которая создает папки внутри основной папки
def make_dir(name_dir):
    name_dir_path = os.path.join(name_base_dir_path, f'{name_dir}')
    if not os.path.exists(name_dir_path):
        os.mkdir(name_dir_path)
    else:
        print(f'Дириктория с именем {name_dir} уже существует, введите другое имя')


make_dir('settings') # создаем папочки в нашей основной папке my_project
make_dir('mainapp')
make_dir('admapp')
make_dir('authapp')

# settings = os.path.join(my_project, 'settings')
# if not os.path.exists(settings):
#     os.mkdir(settings)
# else:
#     print('Такая дириктория уже существует, введите другое имя')
#
# mainapp = os.path.join(my_project, 'mainapp')
# if not os.path.exists(mainapp):
#     os.mkdir(mainapp)
# else:
#     print('Такая дириктория уже существует, введите другое имя')
#
# adminapp = os.path.join(my_project, 'adminapp')
# if not os.path.exists(adminapp):
#     os.mkdir(adminapp)
# else:
#     print('Такая дириктория уже существует, введите другое имя')
#
# authapp = os.path.join(my_project, 'authapp')
# if not os.path.exists(authapp):
#     os.mkdir(authapp)
# else:
#     print('Такая дириктория уже существует, введите другое имя')
