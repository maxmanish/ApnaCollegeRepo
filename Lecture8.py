class Account:
    def __init__(self, balance, accnum):
        self.balance=balance
        self.accnum=accnum
    def debit(self,debitamount):
        self.balance=self.balance-debitamount
        print(debitamount, "debited from",self.accnum,". Updated balance =",self.balance)
    def credit(self,creditamount):
        self.balance=self.balance+creditamount
        print(creditamount, "credited from",self.accnum,". Updated balance =",self.balance)

a1=Account(10000,12345)
a1.debit(500)
a1.credit(3000)
a1.credit(100)
