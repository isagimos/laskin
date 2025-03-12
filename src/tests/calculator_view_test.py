import unittest
from tkinter import Tk
from ui.calculator_view import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator(Tk())

    def test_operands_and_operator_are_none_at_startup(self):
        self.assertEqual(self.calculator._first_operand, None)
        self.assertEqual(self.calculator._second_operand, None)
        self.assertEqual(self.calculator._operator, None)
    
    def test_operators_are_determined_correctly(self):
        self.assertEqual(self.calculator._operators, ["+", "-", "*", "/"])