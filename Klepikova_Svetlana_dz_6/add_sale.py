import sys


with open('bakery.csv', 'a', encoding='utf-8') as fw:
    fw.writelines(str(sys.argv[1] + '\n'))
