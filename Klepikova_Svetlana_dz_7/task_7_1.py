import os


# путь до директории, в которой будем создавать папку my_project
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
my_project = os.path.join(BASE_DIR, 'my_project')
if not os.path.exists(my_project):
    os.mkdir(my_project)
else:
    print('Такая дириктория уже существует, введите другое имя')


settings = os.path.join(my_project, 'settings')
if not os.path.exists(settings):
    os.mkdir(settings)
else:
    print('Такая дириктория уже существует, введите другое имя')

mainapp = os.path.join(my_project, 'mainapp')
if not os.path.exists(mainapp):
    os.mkdir(mainapp)
else:
    print('Такая дириктория уже существует, введите другое имя')

adminapp = os.path.join(my_project, 'adminapp')
if not os.path.exists(adminapp):
    os.mkdir(adminapp)
else:
    print('Такая дириктория уже существует, введите другое имя')

authapp = os.path.join(my_project, 'authapp')
if not os.path.exists(authapp):
    os.mkdir(authapp)
else:
    print('Такая дириктория уже существует, введите другое имя')


# def make_dir(name_dir):
#     name_dir = os.path.join(my_project, f'{name_dir}')
#     if not os.path.exists(name_dir):
#         os.mkdir(name_dir)
#     else:
#         print('Такая дириктория уже существует, введите другое имя')
#
#
# make_dir(settings)
