class BankAccount:
    def __init__(self, account_number, balance=0.0):
        self.__account_number = account_number
        self.__balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.__balance:
            raise ValueError("Insufficient funds.")
        self.__balance -= amount

    def update_balance(self, amount):
        if not isinstance(amount, (int, float)):
            raise TypeError("Amount must be a number.")
        self.__balance += amount

    def get_balance(self):
        return self.__balance

    def get_account_number(self):
        return self.__account_number

    def __str__(self):
        return f"Account Number: {self.__account_number} Balance: ${self.__balance:,.2f}"
