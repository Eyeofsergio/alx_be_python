# Create class definition to bank account

class BankAccount:
    def _init_(self, initial_balance=0):
        self._account_balance = initial_balance 

# Def class for Deposit
 
    def deposit(self, amount):
        if amount > 0:
            self._account_balance = amount 

# Def class for withdraw

    def withdraw (self, amount):
        if amount > 0 and self._account_balance >= amount:
            self._account_balance = amount
            return True
        return False

# Display Balance

    def display_balance(self):
        print(f"Current Balance: {self._account_balance}")

    def get_balance(self):
        return self._account_balance
    
    