#CREATE A ACCOUNTclass WITH
#->ATTRIBUTES-BALAMCE,ACCOUNT NUMBER
#->METHODS-DEBIT,CREDIT,PRINT BALANCE
class account:
    def __init__(self,balance,accountnumber):
        self.balance=balance
        self.accountnumber=accountnumber
    def debit(self):
        print("amount debited")
    def credit(self):
        print('amount credited')
    def print_balance(self):
        print(self.balance)
#creating object
a=account(10000,6355161453)
a.debit()
a.credit()
a.print_balance()