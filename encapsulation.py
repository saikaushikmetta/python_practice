class aaccount:
    def __init__(self,bal):
        self.__balance=bal#here when we use"__"before any variable it becomes private
    def show_balance(self):
        print("balance",self.__balance)
a=aaccount(100)
a.show_balance()