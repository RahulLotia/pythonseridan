from Account_Exceptions import Insufficent_Balance_Error,Incorrect_Amount_Error,Overdraft_Limit_Error,Minimum_Balance_Error
from Accounts import Account

class ChequingAccount(Account):
    def __init__(self, customer_id, name, accountNum, balance=0.0):
        super().__init__(customer_id, name, accountNum)
        self.__balance = balance
        
    def withdraw(self, amount:float):
        if amount > (2000 + int(self.__balance)):
            raise Overdraft_Limit_Error()    
        else:
            self.__balance = self.__balance - amount
         
        return self.__balance
    
    def deposit(self, amount:float):
        if amount <= 0:
            raise Incorrect_Amount_Error()    
        else:
            self.__balance += amount
        
        return self.__balance 
    
    def __str__(self):
        return super(ChequingAccount, self).__str__() +f" {self.__balance}"
