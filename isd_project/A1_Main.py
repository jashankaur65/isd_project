from client.client import Client
from bank_account.bank_account import BankAccount

def main():
    client = Client("Susan", "Clark", "susanclark@pixell.com", 1010)
    account = BankAccount(20019, 6764.67)

    print(client)
    print(account)

if __name__ == "__main__":
    main()
