# 10/05/2025

class BankAccount:
    def __init__(self, account_holder, balance=0):
        """ Initializes the bank account with the account holder's name and an initial balance (default is 0) """
        self.account_name = account_holder
        self.balance = balance

    def deposit(self, amount):
        """ Deposits the given amount into the account """
        if amount > 0:
            self.balance += amount
        else:
            print("Deposit amount must be greater than 0.")
        
    def withdraw(self, amount):
        """ Withdraws the given amount from the account. If the balance is insufficient, it should print an error message """
        if amount <= self.balance:
            self.balance -= amount
        else:
            return print("Insufficient funds.")

    def get_balance(self):
        """ Returns the current balance of the account """
        return self.balance

    def transfer(self, other_account, amount):
        """ Transfers the given amount to another bank account. 
            If the balance is insufficient, it should print an error message. 
            Otherwise, it should withdraw the amount from the current account and deposit it into the other account.
        """
        if amount <= self.balance:
            self.balance -= amount
            other_account.balance += amount
        else:
            print("Insufficient funds.")