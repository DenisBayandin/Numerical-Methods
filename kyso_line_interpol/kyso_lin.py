array_x = [1, 2, 4, 5, 8]
array_y = [-1, -2, 1, 3, 3]

def range_x(array_x, x):
    for i in range(len(array_x)):
        if i+1 >= len(array_x):
            print("\nОшибка: вы вышли за рамки массива, возможно из-за того, что число X не принадлежит ни одному из интервалов [Xi, Xi+1]\n")
            raise IndexError("Введите другой Х")
        else:
            if x >= array_x[i] and x <= array_x[i+1]:
                print(f"\nX принадлежит интервалу [{array_x[i]},{array_x[i+1]}]\n")
                return kys_lin_interp(array_x, array_y, i, x)


def kys_lin_interp(array_x, array_y, i, x):
    deli = (array_y[i+1] - array_y[i])/(array_x[i+1] - array_x[i])
    F = array_y[i] + deli * (x - array_x[i])
    return F

x = float(input("Введите значение X: "))
print(f"F({x}) = {range_x(array_x, x)}")