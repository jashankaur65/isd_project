import unittest
from bank_account.bank_account import BankAccount

class TestBankAccount(unittest.TestCase):
    def setUp(self):
        self.account = BankAccount(20019, 500)

    def test_deposit(self):
        self.account.deposit(100)
        self.assertEqual(self.account.get_balance(), 600)

    def test_withdraw(self):
        self.account.withdraw(100)
        self.assertEqual(self.account.get_balance(), 400)

    def test_withdraw_insufficient(self):
        with self.assertRaises(ValueError):
            self.account.withdraw(1000)

    def test_deposit_invalid(self):
        with self.assertRaises(ValueError):
            self.account.deposit(-100)

    def test_update_balance(self):
        self.account.update_balance(50)
        self.assertEqual(self.account.get_balance(), 550)

    def test_str(self):
        self.assertEqual(str(self.account), "Account Number: 20019 Balance: $500.00")
