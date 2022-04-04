from Consumer import Consumer

class Account(Consumer):
    
    def __init__(self, customer_id, name, accountNum):
        super().__init__(customer_id, name)
        self._accountNum = accountNum
        
    def withdraw(self, amount:float):
        pass
    
    def deposit(self, amount:float):
        pass
    
    def __str__(self):
        return super(Account, self).__str__() + f" {self._accountNum}"