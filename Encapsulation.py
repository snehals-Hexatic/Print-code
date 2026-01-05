
class BankAccount:
    def __init__(self,balance):
        self.__balance = balance  # private Variable
        
    def deposit(self, amount):
        self.__balance +=amount
        print("Deposited:",amount)
        
    def show_balance(self):
        print("Balance:", self.__balance)
        
acc = BankAccount(1000)

acc.deposit(500)
acc.show_balance()
# print(acc.__balance)   
