from itertools import zip_longest


tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена', 'Аккакий', 'Аркадий', 'Кира']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']


def check_gen(tutors: list, klasses: list):
    for i in range(len(tutors)):
        yield tutors[i], klasses[i] if i < len(klasses) else None


generator = check_gen(tutors, klasses)
# добавьте здесь доказательство, что создали именно генератор
for _ in range(len(tutors)):
    print(next(generator))
#next(generator)  # если раскомментировать, то должно падать в traceback по StopIteration

# Решение 1
#print(*{key: val for key, val in zip_longest(tutors, klasses)}.items(), sep='\n')

# Решение 2
# d = dict.fromkeys(tutors) | dict(zip(tutors, klasses))
# print(*d.items(), sep='\n')

# #Решение 3
# di = dict(zip(tutors, klasses))
# for key in tutors:
#     r = di.setdefault(key)
#
# print(*di.items(), sep='\n')

# Решение 4
# d = dict(zip(tutors, klasses))
# d = {key: d.get(key) for key in tutors}
# print(d)
# print(type(d))
#
#
# generator = check_gen(tutors, klasses)
