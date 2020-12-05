group_28 = ['Митя', 'Данил', 'Никита', 'Гриша', 'Анастасия']
group_28_2 = 'Митя', 'Данил', 'Никита', \
             'Гриша', 'Анастасия'

print(group_28_2)

print(type(group_28), group_28.__sizeof__())  # CD-RW, mutable
print(type(group_28_2), group_28.__sizeof__())  # CD-R, immutable
# CD-R VS CD-RW

# mutable: list, dict, set
# immutable: tuple, int, float, str

for student in group_28:
    print(student)
