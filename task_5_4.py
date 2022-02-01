def get_numbers(src: list):
    res = (num for num in len(src) if src[num] > src[num - 1])
    return res


src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
print(*get_numbers(src))