group_28 = [
    ['Митя', '5', '4', '5', '3', '5', '3', '4'],
    ['Данил', '5', '4', '5', '3', '5', '3', '4'],
    ['Никита', '5', '4', '5', '3', '5', '3', '4'],
    ['Гриша', '5', '4', '5', '3', '5', '3', '4'],
    ['Анастасия', '5', '4', '5', '3', '5', '3', '4']
]


def show_student(student_record):
    # print(student_record[0], student_record[1:])
    print(student_record[0], ':', ', '.join(student_record[1:]))


for record in group_28:
    show_student(record)
