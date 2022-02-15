class BankAccount():
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
    def deposit(self,amount):
        if amount >= 0:
            self.balance = self.balance + amount
    def withdraw(self, amount):
        if amount >=0 and amount < self.balance:
            self.balance = self.balance - amount

if __name__ == '__main__':
    ba = BankAccount("Chase", 100)
    print(ba.balance)
    ba.withdraw(50)
    print(ba.balance)