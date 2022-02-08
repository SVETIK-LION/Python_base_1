import sys


with open('bakery.csv', 'r', encoding='utf-8') as fr:
    length = len(sys.argv) # длина, в зависимости от кол-ва параметров
    if length == 1:
        for line in fr.readlines():
            print(line.strip())
    elif length == 2:
        start = int(sys.argv[1])
        for line in fr.readlines()[start - 1:]:
            print(line.strip())
    elif length == 3:
        start = int(sys.argv[1])
        end = int(sys.argv[2])
        for line in fr.readlines()[start - 1:end]:
            print(line.strip())
