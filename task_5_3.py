tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']


def check_gen(tutors: list, klasses: list):
    di = dict(zip(tutors, klasses))
    result = {key: val for tutors, klasses in di.items()}
    return result


generator = check_gen(tutors, klasses)

# добавьте здесь доказательство, что создали именно генератор
#print(type(result))
for _ in range(len(tutors)):
    print(next(generator))
# next(generator)  # если раскомментировать, то должно падать в traceback по StopIteration