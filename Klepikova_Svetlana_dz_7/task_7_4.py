import os.path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
folder = os.path.join(BASE_DIR, 'my_project')
border_1 = 10
border_2 = 100
border_3 = 1000
border_4 = 10000
count_1 = 0
count_2 = 0
count_3 = 0
count_4 = 0
for item in os.listdir(folder):
    file_size = os.stat(os.path.join(folder, item)).st_size
    if file_size <= border_1:
        count_1 += 1
    elif file_size <= border_2:
        count_2 += 1
    elif file_size <= border_3:
        count_3 += 1
    elif file_size <= border_4:
        count_4 += 1
dict_size = {border_1: count_1,
             border_2: count_2,
             border_3: count_3,
             border_4: count_4}
print(dict_size)
