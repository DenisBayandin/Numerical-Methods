# Так как у нас все х упорядочены, значит мы применяем кусочно-линейную интерполяцию

x=[1, 2, 4, 5, 8]
y=[-1, -2, 1, 3, 3]

# Так как у нас 3 узла, то нужно искомая интерполяция по формуле Лагранжа будет иметь вторую степень ( число узлов - 1)

def form_Lagranza(x_array, y_array, new_x):
    virazenie = 0
    for j in range(len(y)):
        proiz_verxa = 1;
        proiz_niza = 1
        for i in range(len(x)):
            if i == j:
                proiz_verxa = proiz_verxa * 1;
                proiz_niza = proiz_niza * 1
            else:
            # умножаем каждый раз, потому что мы находим произведение скобок, если у нас три узла, то мы должны перемножить две скобки, так как степень = 2, если 4 узла, то три скобки, так как степень = 3 и т.д.
                proiz_verxa *= (new_x - x[i])
                proiz_niza *= (x[j] - x[i])
        # После того, как мы прошлись по всем возможным "x", мы переходим на следующий "y" складываем и снова перемножаем все скобки
        virazenie += y[j] * proiz_verxa / proiz_niza
    return virazenie

print(round(form_Lagranza(x, y, 2.5), 3))