group_28 = [
    ['Митя', '5', '4', '5', '3', '5', '3', '4'],
    ['Данил', '5', '4', '5', '3', '5', '3', '4'],
    ['Никита', '5', '4', '5', '3', '5', '3', '4'],
    ['Гриша', '5', '4', '5', '3', '5', '3', '4'],
    ['Анастасия', '5', '4', '5', '3', '5', '3', '4']
]


def show_student(student_record):
    # print(student_record[0], student_record[1:])
    # print(student_record[0], ':', ', '.join(student_record[1:]))
    marks = student_record[1:]
    marks_as_int = []
    for mark in marks:
        mark = int(mark)
        marks_as_int.append(mark)

        # print(mark, type(mark))
     # print(marks_as_int)
    marks_avg = sum(marks_as_int) / len(marks_as_int)
    marks_as_str = ', ' .join(marks)
    print(f'{student_record[0]}: {marks_as_str}, средний балл {marks_avg}')


for record in group_28:
    show_student(record)
