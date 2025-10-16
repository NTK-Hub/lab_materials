import unittest
from calculator import execute_operation


class TestCalculator(unittest.TestCase):

    def test_addition(self):
        """Сложение чисел"""
        self.assertEqual(execute_operation(12, 8, '+'), 20)
        self.assertEqual(execute_operation(-2, 2, '+'), 0)
        self.assertEqual(execute_operation(0, 5, '+'), 5)

    def test_subtraction(self):
        """Вычитание чисел"""
        self.assertEqual(execute_operation(15, 5, '-'), 10)
        self.assertEqual(execute_operation(2, 7, '-'), -5)

    def test_multiplication(self):
        """Умножение чисел"""
        self.assertEqual(execute_operation(4, 6, '*'), 24)
        self.assertEqual(execute_operation(-3, 5, '*'), -15)
        self.assertEqual(execute_operation(0, 10, '*'), 0)

    def test_division(self):
        """Деление чисел"""
        self.assertEqual(execute_operation(20, 4, '/'), 5)
        self.assertEqual(execute_operation(7, 2, '/'), 3.5)

    def test_division_by_zero(self):
        """Деление на ноль (ошибка)"""
        self.assertEqual(execute_operation(5, 0, '/'), "Ошибка: деление на ноль невозможно.")

    def test_modulo(self):
        """Деление по модулю"""
        self.assertEqual(execute_operation(20, 6, '%'), 2)
        self.assertEqual(execute_operation(12, 4, '%'), 0)

    def test_modulo_by_zero(self):
        """Деление по модулю на ноль (ошибка)"""
        self.assertEqual(execute_operation(5, 0, '%'), "Ошибка: деление на ноль невозможно.")

    def test_power(self):
        """Возведение в степень"""
        self.assertEqual(execute_operation(3, 3, '**'), 27)
        self.assertEqual(execute_operation(9, 0, '**'), 1)
        self.assertEqual(execute_operation(2, 10, '**'), 1024)

    def test_square_root(self):
        """Извлечение квадратного корня"""
        self.assertEqual(execute_operation(25, 0, 'sqrt'), 5)
        self.assertEqual(execute_operation(0, 0, 'sqrt'), 0)
        self.assertEqual(execute_operation(2.25, 0, 'sqrt'), 1.5)

    def test_square_root_negative(self):
        """Корень из отрицательного числа (ошибка)"""
        self.assertEqual(execute_operation(-9, 0, 'sqrt'), "Ошибка: нельзя извлечь корень из отрицательного числа.")

    def test_factorial(self):
        """Факториал числа"""
        self.assertEqual(execute_operation(6, 0, '!'), 720)
        self.assertEqual(execute_operation(0, 0, '!'), 1)
        self.assertEqual(execute_operation(1, 0, '!'), 1)
        self.assertEqual(execute_operation(4, 0, '!'), 24)

    def test_factorial_negative(self):
        """Факториал отрицательного числа (ошибка)"""
        self.assertEqual(execute_operation(-1, 0, '!'), "Ошибка: факториал отрицательных чисел не существует.")

    def test_factorial_decimal(self):
        """Факториал нецелого числа (ошибка)"""
        self.assertEqual(execute_operation(2.5, 0, '!'), "Ошибка: факториал определён только для целых чисел.")

    def test_factorial_too_large(self):
        """Факториал слишком большого числа (ошибка)"""
        self.assertEqual(execute_operation(150, 0, '!'), "Ошибка: число слишком велико для вычисления факториала.")

    def test_large_numbers(self):
        """Работа с большими числами"""
        self.assertEqual(execute_operation(500000, 500000, '+'), 1000000)
        self.assertEqual(execute_operation(2, 10, '**'), 1024)

    def test_decimal_precision(self):
        """Проверка точности вычислений"""
        result = execute_operation(0.2, 0.3, '+')
        self.assertAlmostEqual(result, 0.5, places=7)
        result = execute_operation(2, 3, '/')
        self.assertAlmostEqual(result, 0.6666667, places=7)

    def test_negative_operations(self):
        """Операции с отрицательными числами"""
        self.assertEqual(execute_operation(-7, -3, '+'), -10)
        self.assertEqual(execute_operation(-2, 4, '*'), -8)
        self.assertEqual(execute_operation(-20, 5, '/'), -4)

if __name__ == '__main__':
    unittest.main(verbosity=2)