import math
from scipy import integrate

pi = math.pi

T = [-0.77460, 0, 0.77460]
C = [0.55555555555, 0.88888888888, 0.55555555555]


def X_i(a, b, t):
    x_i = []
    for i in range(0,3):
        X = (a+b)/2 + (b-a)/2 * t[i]
        print(f"X_{i} = {round(X, 5)}")
        x_i.append(round(X, 5))
    return x_i


def F_X_i_no_sin(x_i):
    func = []
    for i in range(0, 3):
        func_i = 6 * (x_i[i]**5) + 3 * (x_i[i]**2)
        print(f"F_x_{i} = {func_i}")
        func.append(func_i)
    return func


def F_X_i_yes_sin(x_i):
    func = []
    for i in range(0, 3):
        func_i = math.sin(x_i[i])
        print(f"F_x_{i} = {func_i}")
        func.append(func_i)
    return func


def func(a, b, f_x_i, C):
    result = (b-a)/2
    result_parentheses = 0
    for i in range(0, 3):
        result_parentheses += C[i] * f_x_i[i]
    print(f"Результат интеграла: {result * result_parentheses}")


# def fault(a, b, n):
#     pogrestn_1 = (b-a)**(2*n+1) * math.factorial(n)**4
#     pogrestn_2 = math.factorial(2*n)**3 * (2 * n + 1)
#     # M =
#     pogrestn = pogrestn_1/pogrestn_2
#     print(f"Погрешность = {pogrestn}")


# Решаем первый интеграл с помощью метода Гаусса
a = 0
b = 2
x_i = X_i(a, b, T)
f_x_i = F_X_i_no_sin(x_i)
func(a, b, f_x_i, C)
# Находим интеграл начальной формулы
init_formul = lambda x: 6 * (x**5) + 3 * (x**2)
integ = integrate.quad(init_formul, 0, 2)
print(f"Результат интеграла без метода Гаусса = {integ[0]}")
# Погрешность
# fault(a, b, 3)

print("\n")
for i in range(1, 50):
    print("_", end="")
print("\n\n")


# Решаем второй интеграл с помощью метода Гаусса
a = 0
b = pi
x_i = X_i(a, b, T)
f_x_i = F_X_i_yes_sin(x_i)
func(a, b, f_x_i, C)
# Находим интеграл начальной формулы
init_formul = lambda x: math.sin(x)
integ = integrate.quad(init_formul, 0, pi)
print(f"Результат интеграла без метода Гаусса = {integ[0]}")
# Погрешность
# fault(a, b, 3)

