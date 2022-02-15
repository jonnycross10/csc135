class BankAccount:
    def __init__(self,name):
        self.name = name
        self.balance = 0
        self.transaction_fee = 0
    
    @property
    def transaction_fee(self):
        return self.transaction_fee
    
    @transaction_fee.setter
    def transaction_fee(self, value):
        if value <0:
            return
        else:
            self.transaction_fee = value
            return

    def deposit(self,amount):
        if amount >= 0:
            self.balance = self.balance + amount
    def withdraw(self, amount):
        amount_pos = amount >= 0 
        t_fee_pos = self.transaction_fee >=0
        no_neg_bal = amount <= self.balance
        no_high_fee = amount + self.transaction_fee <= self.balance
        if amount_pos and t_fee_pos and no_neg_bal and no_high_fee :
            self.balance = self.balance - (amount + self.transaction_fee)
    

if __name__ == '__main__':
    ba = BankAccount("Chase")
    print(ba.balance)
    ba.deposit(100)
    ba.transaction_fee = 5
    ba.transaction_fee= -1
    ba.withdraw(50)
    print(ba.balance)
    # wife_acc = BankAccount("Wells")
    # wife_acc.withdraw(190)
    # print(wife_acc.balance)