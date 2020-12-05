# DRY -> ?
# функции

def calc_rectangle_area(w, h):
    return w * h


area = calc_rectangle_area(15, 20)  # call -> return -> 300
print('площадь прямоугольника', area)

area = calc_rectangle_area(10, 30)
print('площадь прямоугольника', area)

w = 5
h = 25
area = calc_rectangle_area(5, 25)
print('площадь прямоугольника', area)
