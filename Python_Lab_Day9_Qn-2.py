class Account:
    def __init__(self, hName, balance):
        self._holderName = hName
        self._balance = balance

    def __add__(self, other):
        return self._balance + other._balance

class SavingsAccount(Account):
    def calculate_interest(self):
        return self._balance * 0.05
    
class CurrentAccount(Account):
    def calculate_interest(self):
        return self._balance * 0.02
    
savings_account = SavingsAccount("Ravi", 10000)
current_account = CurrentAccount("Anjali", 15000)

print("Savings account: ")
print(f"Name: {savings_account._holderName}")
print(f"Balance: {savings_account._balance}")
print(f"Interest: {savings_account.calculate_interest()}")

print()