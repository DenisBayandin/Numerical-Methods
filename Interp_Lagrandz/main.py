# Так как у нас все х упорядочены, значит мы применяем кусочно-линейную интерполяцию
# Так как у нас 3 узла, то нужно искомая интерполяция по формуле Лагранжа будет иметь вторую степень ( число узлов - 1)

def form_Lagranza(x_array, y_array, new_x):
    virazenie = 0
    for j in range(len(y_array)):
        proiz_verxa = 1;
        proiz_niza = 1
        for i in range(len(x_array)):
            if i == j:
                proiz_verxa = proiz_verxa * 1;
                proiz_niza = proiz_niza * 1
            else:
            # умножаем каждый раз, потому что мы находим произведение скобок, если у нас три узла, то мы должны перемножить две скобки, так как степень = 2, если 4 узла, то три скобки, так как степень = 3 и т.д.
                proiz_verxa *= (new_x - x_array[i])
                proiz_niza *= (x_array[j] - x_array[i])
        # После того, как мы прошлись по всем возможным "x", мы переходим на следующий "y" складываем и снова перемножаем все скобки
        virazenie += y_array[j] * proiz_verxa / proiz_niza
    return virazenie


def vi4islenie_func(x_array):
    y = []
    for i in x_array:
        func_y = i**4 + 1
        y.append(func_y)
    return y

x = [1, 2, 4, 5, 8]
y = [-1, -2, 1, 3, 3]
print("\nВычисления при уже известных 'x' and 'y': ", round(form_Lagranza(x, y, 8), 3))
new_array_y = vi4islenie_func(x)
print("\nСоздаем новый массив 'y' при уже известном массиве 'x': ", new_array_y)
print("\nВычисления при известном массиве 'x' и только что созданом массиве 'y': ",
round(form_Lagranza(x, new_array_y, 8), 3))

