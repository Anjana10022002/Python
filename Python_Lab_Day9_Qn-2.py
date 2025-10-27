class Account:
    def __init__ (self, hName, balance):
        self._holderName = hName
        self._balance = balance

    def __add__ (self, other):
        return self._balance + other._balance

class SavingsAccount(Account):
    def calculate_interest(self):
        return self._balance * 0.05

    

savingsAccount1 = Account("Ravi", 10000)
savingsAccount2 = Account("Anjali", 15000)

print(savingsAccount1)
    
