def show_student(group, student):
    print('Студент группы', group, ':', student)


def show_group(group, students):
    for student in students:
        print('Студент группы', group, ':', student)


group_28 = ['Митя', 'Данил', 'Никита', 'Гриша', 'Анастасия']
show_group('28', group_28)

group_38 = ['Пётр', 'Вася', 'Иван']
show_group('38', group_38)
