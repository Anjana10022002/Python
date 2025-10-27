class Account:
    def __init__ (self, hName, balance):
        self._holderName = hName
        self._balance = balance

    
class SavingsAccount(Account):
    def __init__(self, hName, balance):
        super().__init__(hName, balance)
        claculate_interest = balance * 0.02
        return claculate_interest
