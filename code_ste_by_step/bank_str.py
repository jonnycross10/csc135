class BankAccount:
    def __init__(self,name):
        self.name = name
        self.balance = 0
    
    def __str__(self):
        return "{}, ${}".format(self.name, str(round(self.balance,2)))

    def deposit(self,amount):
        if amount >= 0:
            self.balance = self.balance + amount
    def withdraw(self, amount):
        amount_pos = amount >= 0 
        no_neg_bal = amount <= self.balance
        if amount_pos and no_neg_bal:
            self.balance = self.balance - amount 

if __name__ == '__main__':
    ba = BankAccount("Chase")
    ba.deposit(100.977)
    print(str(ba))
