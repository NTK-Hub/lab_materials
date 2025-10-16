import operator
import math


def read_number(message):
    """Запрашивает у пользователя число и проверяет корректность ввода."""
    while True:
        try:
            return float(input(message))
        except ValueError:
            print("Ошибка ввода: требуется числовое значение.")


def choose_operation():
    """Предлагает пользователю выбрать одну из доступных операций или завершить программу."""
    available_ops = ['+', '-', '*', '/', '%', '**', 'sqrt', '!', 'q']
    while True:
        op = input(f"Выберите операцию ({', '.join(available_ops[:-1])}) или 'q' для выхода: ")
        if op in available_ops:
            return op
        print("Операция не распознана. Повторите ввод.")


def execute_operation(a, b, op):
    """Выполняет выбранную пользователем операцию над числами."""
    math_ops = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv,
        '%': operator.mod,
        '**': operator.pow
    }

    if op == 'sqrt':
        return square_root(a)
    if op == '!':
        return factorial_calc(a)

    try:
        return math_ops[op](a, b)
    except ZeroDivisionError:
        return "Ошибка: деление на ноль невозможно."


def square_root(x):
    """Возвращает квадратный корень числа или сообщение об ошибке."""
    if x < 0:
        return "Ошибка: нельзя извлечь корень из отрицательного числа."
    return math.sqrt(x)


def factorial_calc(n):
    """Вычисляет факториал целого числа с проверкой допустимости."""
    if n != int(n):
        return "Ошибка: факториал определён только для целых чисел."
    if n < 0:
        return "Ошибка: факториал отрицательных чисел не существует."
    if n > 100:
        return "Ошибка: число слишком велико для вычисления факториала."

    return math.factorial(int(n))


def run_calculator():
    """Основной цикл работы калькулятора."""
    print("=== Простой калькулятор ===")
    print("Операции: +, -, *, /, %, **, sqrt, !")
    print("Для выхода введите 'q' при выборе операции.\n")

    while True:
        op = choose_operation()

        if op == 'q':
            print("Работа программы завершена.")
            break

        # Для операций с одним аргументом
        if op in ['sqrt', '!']:
            x = read_number("Введите число: ")
            y = 0
        else:
            x = read_number("Введите первое число: ")
            y = read_number("Введите второе число: ")

        result = execute_operation(x, y, op)
        print(f"Ответ: {result}\n")


if __name__ == "__main__":
    run_calculator()
