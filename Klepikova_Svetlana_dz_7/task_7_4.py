import os.path


border_1 = 10
border_2 = 100
border_3 = 1000
border_4 = 10000
count_1 = 0
count_2 = 0
count_3 = 0
count_4 = 0
for root, dirs, files in os.walk('my_project'):
    if files:
        for file in files:
            file_size = os.stat(os.path.join(root, file)).st_size
            if file_size <= border_1:
                count_1 += 1
            elif border_1 < file_size <= border_2:
                count_2 += 1
            elif border_2 < file_size <= border_3:
                count_3 += 1
            elif border_3 < file_size <= border_4:
                count_4 += 1
dict_size = {border_1: count_1,
             border_2: count_2,
             border_3: count_3,
             border_4: count_4}
print(dict_size)
