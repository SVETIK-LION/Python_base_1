def sum_list_1(dataset: list) -> int:
    """Вычисляет сумму чисел списка dataset, сумма цифр которых делится нацело на 7"""
    sum_digits = 0
    sum_num = 0
    for i in dataset:
        copy_i = i
        while copy_i > 0:
            digit = copy_i % 10
            sum_digits += digit
            copy_i //= 10
        if sum_digits % 7 == 0:
            sum_num += i
        sum_digits = 0
    return sum_num


def sum_list_2(dataset: list) -> int:
    """К каждому элементу списка добавляет 17 и вычисляет сумму чисел списка, сумма цифр которых делится нацело на 7"""
    for i in range(len(dataset)):
        dataset[i] += 17
    return sum_list_1(dataset)


my_list = [n**3 for n in range(1, 1000, 2)] #Собрали список кубов от 1 до 1000
result_1 = sum_list_1(my_list)
print(result_1)
result_2 = sum_list_2(my_list)
print(result_2)