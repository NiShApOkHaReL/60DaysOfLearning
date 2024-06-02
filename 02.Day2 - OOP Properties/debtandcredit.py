class Account:
    def __init__(self, bal, acc):
        self.balance = bal
        self.account = acc

    def debit(self, debamount):
        self.balance -= debamount
        print("Rs.",debamount,"was debited.")
        print("Total balance is", self.get_balance())

    def credit(self, creamount):
        self.balance += creamount
        print("Rs.",creamount,"was credited")
        print("Total balance is", self.get_balance())


    def get_balance(self):
        return self.balance
    
acc = Account(1000,123)
acc.debit(100)
acc.credit(500)
acc.get_balance()




