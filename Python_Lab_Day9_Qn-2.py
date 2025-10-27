class Account:
    def __init__ (self, hName, balance):
        self._holderName = hName
        self._balance = balance

    def __add__ (self, other):
        return self._balance + other._balance

class SavingsAccount(Account):
    def calculate_interest(self):
        return self._balance * 0.05
    
class CurrentAccount(Account):
    def calculate_interest(self):
        return self._balance * 0.02
    
savings_account1 = Account("Ravi", 10000)
savings_account2 = Account("Anjali", 15000)

print()
    
