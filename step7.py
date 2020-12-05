group_28 = [
    ['Митя', '5', '4', '5', '3', '5', '3', '4'],
    ['Данил', '5', '4', '5', '3', '5', '3', '4'],
    ['Никита', '5', '4', '5', '3', '5', '3', '4'],
    ['Гриша', '5', '4', '5', '3', '5', '3', '4'],
    ['Анастасия', '5', '4', '5', '3', '5', '3', '4']
]


def show_student(student_record):
    marks = student_record[1:]
    marks_as_int = map(int, marks)
    marks_avg = sum(marks_as_int) / len(marks)
    marks_as_str = ', ' .join(marks)
    print(f'{student_record[0]}: {marks_as_str}, средний балл {marks_avg}')


for record in group_28:
    show_student(record)

# result = map(show_student, group_28)
# print(*result)
# next(result)
# next(result)
# next(result)
# next(result)
# next(result)