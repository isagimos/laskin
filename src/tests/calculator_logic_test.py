import unittest
from tkinter import Tk
from services.calculator_logic import CalculatorLogic

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = CalculatorLogic()
        self.username = "test_username"

    def test_if_entry_value_is_empty_button_is_not_added(self):
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

    def test_operand_is_not_added_if_there_is_already_one(self):
        self.calculator._operator = "+"
        return_value = self.calculator.handle_click("111+", "*", self.username)
        self.assertEqual(return_value, "111+")

    def test_divide_by_zero(self):
        self.calculator._first_operand = "4"
        self.calculator._operator = "/"

        return_value = self.calculator.handle_click("4/0", "=", self.username)
        self.assertEqual(return_value, "Virhe")

    def test_operand_cannot_start_by_two_or_more_zeros(self):
        return_value = self.calculator.handle_click("0", "0", self.username)
        self.assertEqual(return_value, "0")
        return_value2 = self.calculator.handle_click("12*0", "0", self.username)
        self.assertEqual(return_value2, "12*0")

    def test_two_or_more_operators_in_a_row_not_accepted(self):
        return_value = self.calculator.handle_click("1+", "+", self.username)
        self.assertEqual(return_value, "1+")

    def test_operator_not_accepted_at_start(self):
        return_value = self.calculator.handle_click("", "/", self.username)
        self.assertEqual(return_value, "")