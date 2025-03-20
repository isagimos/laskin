import unittest
from tkinter import Tk
from services.calculator_logic import CalculatorLogic

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = CalculatorLogic()
        self.username = "test_username"

    def test_operands_and_operator_are_none_at_startup(self):
        self.assertEqual(self.calculator._first_operand, None)
        self.assertEqual(self.calculator._second_operand, None)
        self.assertEqual(self.calculator._operator, None)
    
    def test_operators_are_determined_correctly(self):
        self.assertEqual(self.calculator._operators, ["+", "-", "*", "/"])

    def test_at_first_clicking_equals_button_is_not_added(self):
        return_value = self.calculator.handle_click("", "=", self.username)
        self.assertEqual(return_value, "")
    
    def test_at_first_clicking_operator_button_is_not_added(self):
        return_value = self.calculator.handle_click("", "+", self.username)
        self.assertEqual(return_value, "")
        return_value = self.calculator.handle_click("", "-", self.username)
        self.assertEqual(return_value, "")
        return_value = self.calculator.handle_click("", "*", self.username)
        self.assertEqual(return_value, "")
        return_value = self.calculator.handle_click("", "/", self.username)
        self.assertEqual(return_value, "")

    def test_if_button_is_digit_return_entry_value_plus_button(self):
        return_value = self.calculator.handle_click("", "1", self.username)
        self.assertEqual(return_value, "1")

    def test_clicking_operand_button_saves_first_operand_and_operator(self):
        return_value = self.calculator.handle_click("111", "+", self.username)
        self.assertEqual(self.calculator._first_operand, "111")
        self.assertEqual(self.calculator._operator, "+")
        self.assertEqual(return_value, "111+")

    def test_operand_is_not_added_if_there_is_already_one(self):
        self.calculator._operator = "+"
        return_value = self.calculator.handle_click("111+", "*", self.username)
        self.assertEqual(return_value, "111+")
    
    def test_addition_works(self):
        self.calculator._first_operand = "1"
        self.calculator._operator = "+"

        return_value = self.calculator.handle_click("1+2", "=", self.username)
        self.assertEqual(return_value, int("3"))
        
    def test_substraction_works(self):
        self.calculator._first_operand = "1"
        self.calculator._operator = "-"

        return_value = self.calculator.handle_click("1-2", "=", self.username)
        self.assertEqual(return_value, int("-1"))

    def test_multiplication_works(self):
        self.calculator._first_operand = "1"
        self.calculator._operator = "*"

        return_value = self.calculator.handle_click("1*2", "=", self.username)
        self.assertEqual(return_value, int("2"))

    def test_division_works(self):
        self.calculator._first_operand = "4"
        self.calculator._operator = "/"

        return_value = self.calculator.handle_click("4/2", "=", self.username)
        self.assertEqual(return_value, int("2"))

    def test_divide_by_zero(self):
        self.calculator._first_operand = "4"
        self.calculator._operator = "/"

        return_value = self.calculator.handle_click("4/0", "=", self.username)
        self.assertEqual(return_value, "Nollalla ei voi jakaa")