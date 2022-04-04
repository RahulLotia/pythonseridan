from Account_Exceptions import Insufficent_Balance_Error,Incorrect_Amount_Error,Overdraft_Limit_Error,Minimum_Balance_Error
from Accounts import Account

class SavingsAccount(Account):
    
    def __init__(self, customer_id, name, accountNum, balance=0.0):
        super().__init__(customer_id, name, accountNum)
        self.__balance = balance
        
    def withdraw(self, amount:float):
        
        if amount > self.__balance:
            raise Insufficent_Balance_Error()
        
        elif (self.__balance - amount) < 3000:
            raise Minimum_Balance_Error()
            
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
        return super(SavingsAccount, self).__str__() +f" {self.__balance}"