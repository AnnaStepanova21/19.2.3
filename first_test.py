import pytest
from app.calculator import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator

# тест на произведение
    def test_multiply_calculate_correctly(self):
        assert self.calc.multiply(self, 2, 2) == 4

# тест на произведение
    def test_multply_calculation_failed(self):
        assert self.calc.multiply(self, 2, 2) == 5

# тест на деление
    def test_division_calculate_correctly(self):
        assert self.calc.division(self, 8, 4) == 2

# тест на вычитание
    def test_subtraction_calculate_correctly(self):
        assert self.calc.subtraction(self, 8, 3) == 5

# тест на сложение
    def test_adding_calculate_correctly(self):
        assert self.calc.adding(self, 9, 1) == 10