from math import pi, sin

array_x = [pi/6, pi/4, pi/3, pi/2, 2*pi/3]
array_x_string = ["pi/6", "pi/4", "pi/3", "pi/2", "2*pi/3"]


def cos_proiz(array_x):
    array_y = []
    y = 0
    for i in range(len(array_x)):
        y = sin(array_x[i]) * -1 # производная от косинуса
        array_y.append(y)
        print(f"X = {array_x_string[i]}, y = -1 * sinX = {round(y, 4)}\n")
    return array_y


def shag_h(array, count):
    if count==0:
        pass
    else:
        return array[count] - array[count-1]


def left_proiz(array_x, array_y):
    for i in range(len(array_y)):
        if i == 0:
            print("\ni = 0: Невозможно вычислить, так как i-1 нет в таблице (массиве) \n ")
            continue
        else:
            h = shag_h(array_x, i)
            func = (array_y[i] - array_y[i-1])/h
            print(f"X = {array_x_string[i]}, Y = {round(array_y[i], 4)}, func = {round(func, 4)},абсолютная погрешность = {round(func - array_y[i], 4)}")
            # Абсолютная погрешность, дельта = изме. значение - реальное значение.

array_y = cos_proiz(array_x)
left_proiz(array_x, array_y)