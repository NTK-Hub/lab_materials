import numpy as np

# Функция, которую нужно проинтегрировать
def target_function_f(x):
    return np.cos(3*x) * np.log(1.0 + x) + 3.0 * np.sin(x) * np.exp(-0.3*x)

# Производные
def first_derivative(x):
    return -3 * np.sin(3*x) * np.log(1.0 + x) + (3 * np.cos(3*x)) / (1.0 + x) + 3 * np.cos(x) * np.exp(-0.3*x) - 0.3 * 3 * np.sin(x) * np.exp(-0.3*x)

def second_derivative(x):
    return -9 * np.cos(3*x) * np.log(1.0 + x) - (9 * np.sin(3*x)) / (1.0 + x) - (3 * np.cos(3*x)) / ((1.0 + x) ** 2) - 3 * np.sin(x) * np.exp(-0.3*x) - 0.3 * 3 * np.cos(x) * np.exp(-0.3*x) - 0.3 * 3 * np.cos(x) * np.exp(-0.3*x) + 0.09 * 3 * np.sin(x) * np.exp(-0.3*x)

def third_derivative(x):
    return 27 * np.sin(3*x) * np.log(1.0 + x) - (27 * np.cos(3*x)) / (1.0 + x) + (18 * np.sin(3*x)) / ((1.0 + x) ** 2) - (6 * np.cos(3*x)) / ((1.0 + x) ** 3) - 3 * np.cos(x) * np.exp(-0.3*x) - 0.9 * 3 * np.sin(x) * np.exp(-0.3*x) - 0.9 * 3 * np.sin(x) * np.exp(-0.3*x) - 0.09 * 3 * np.cos(x) * np.exp(-0.3*x) - 0.09 * 3 * np.cos(x) * np.exp(-0.3*x) + 0.027 * 3 * np.sin(x) * np.exp(-0.3*x)

def fourth_derivative(x):
    return 81 * np.cos(3*x) * np.log(1.0 + x) + (243 * np.sin(3*x)) / (1.0 + x) + (162 * np.cos(3*x)) / ((1.0 + x) ** 2) - (36 * np.sin(3*x)) / ((1.0 + x) ** 3) + (9 * np.cos(3*x)) / ((1.0 + x) ** 4) + 3 * np.sin(x) * np.exp(-0.3*x) - 0.27 * 3 * np.cos(x) * np.exp(-0.3*x) - 0.27 * 3 * np.cos(x) * np.exp(-0.3*x) - 0.27 * 3 * np.cos(x) * np.exp(-0.3*x) - 0.27 * 3 * np.cos(x) * np.exp(-0.3*x) + 0.081 * 3 * np.sin(x) * np.exp(-0.3*x)

# Вычисление значений производных в точке x=0
f_prime_0 = first_derivative(0)
f_double_prime_0 = second_derivative(0)
f_triple_prime_0 = third_derivative(0)
f_quadruple_prime_0 = fourth_derivative(0)

# Вывод результатов
print("f'(0):", f_prime_0)
print("f''(0):", f_double_prime_0)
print("f'''(0):", f_triple_prime_0)
print("f''''(0):", f_quadruple_prime_0)
