eps = 1e-10  # погрешность


# Функция вывода матрицы на экран
def displayArray(info, a):
    print(info)
    n = len(a)
    for i in range(n):
        line = ""
        for j in range(n + 1):
            line += str("%10.5f" % a[i][j]) + "      "
            if j == n - 1:
                line += "| "
        print(line)
    print("")


# Функция вывода матрицы на экран
def displayArray2(info, a):
    print(info)
    n = len(a)
    for i in range(n):
        line = ""
        for j in range(n):
            line += str("%10.5f" % a[i][j]) + "      "
        print(line)
    print("")


# Функция вывод решения на экран
def displaySolution(x):
    print("Решение системы:")
    for i, val in enumerate(x):
        print("x%x" % (i + 1), " = %5.5f" % val)


# Функция вывода умножения матриц на экран
def displayVec(info, r):
    print(info)
    n = len(r)
    for i in range(n):
        print("%5.5f" % r[i], end="    ")
    print("")


# Нахождение максимально элемента в строке
def maxelement(a, col, count_swap):
    n = len(a)
    maxel = a[col][col]
    maxrow = col
    for i in range(col + 1, n):
        if maxel < abs(a[i][col]):
            maxel = abs(a[i][col])
            maxrow = i
    if col != maxrow:
        swap(a, maxrow, col)
        count_swap += 1
    else:
        print("Перестановка строк не требуется\n")
    return count_swap


# Проверка на ноль
def checkByZero(q):
    if abs(q) < eps:
        return 1


# Вычисление определителя
def determinant(a, count_swap):
    det = 1
    n = len(a)
    if count_swap % 2:
        count_swap = -1
    else:
        count_swap = 1
    for i in range(n):
        det *= a[i][i]
    det *= count_swap
    return det


# Перестановка строк
def swap(a, row_one, row_two=0):
    n = len(a)
    for i in range(n + 1):
        tmp = a[row_one][i]
        a[row_one][i] = a[row_two][i]
        a[row_two][i] = tmp
    displayArray("Перестановка строк", a)


# Вычетание строк
def sub(a, row_one, row_two, mn=1):
    n = len(a)
    for i in range(n + 1):
        a[row_one][i] -= a[row_two][i] * mn
    return a


# Приведение к треугольной матрице
def triangle(a):
    n = len(a)
    count_swap = 0
    for j in range(n - 1):
        print(f"\nШаг {j + 1}:")
        count_swap = maxelement(a, j, count_swap)

        for i in range(j + 1, n):
            c = a[i][j] / a[j][j]
            sub(a, i, j, c)
            print(f"Масштабирующий множитель {j + 1} шага для {i + 1} строки: {c}")
        displayArray("\nПриведение к треугольному виду", a)
    return count_swap


# Нахождение решение, методом обратного хода
def searchSolution(a):
    n = len(a)
    solution = [0 for i in range(n)]
    for i in range(n - 1, -1, -1):
        solution[i] = a[i][n] / a[i][i]
        for j in range(i - 1, -1, -1):
            a[j][n] -= a[j][i] * solution[i]
    return solution


# Метод Гаусса
def gauss(a):
    count_swap = triangle(a)
    x = searchSolution(a)
    return x


# Выделение матрицы B
def getVectorB(a):
    n = len(a)
    vectorB = []
    for i in range(n):
        vectorB.append(a[i][n])
    return vectorB


if __name__ == "__main__":
    import numpy, copy
    from sys import exit

    arr = numpy.loadtxt('input.txt', float)
    clean_arr = copy.deepcopy(arr)
    det = determinant(arr, 0)
    flag = checkByZero(det)
    if flag:
        print("\nМатрица вырожденная. Определитель равен нулю\n")
        exit(0)
    print("\nДанную систему можно решить. Определитель: %5.5f" % det)

    print(f"\nТекущая погрешность: {eps}")
    displayArray("\nНачальная матрица", arr)

    print("\n")
    for i in range(1, 50):
        print("_", end="")
    print("\n\n")

    # Метод Гаусса
    count_swap = triangle(arr)

    print("\n")
    for i in range(1, 50):
        print("_", end="")
    print("\n\n")

    displayArray("\n\nКонечная треугольная матрица", arr)
    x = searchSolution(arr)
    displaySolution(x)