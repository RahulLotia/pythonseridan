class Insufficent_Balance_Error(Exception):
    def __str__(self):
        return f'Insufficient balance in the account. Cannot withdraw.'
    
class Minimum_Balance_Error(Exception):
    def __str__(self):
        return f"You must maintain minimum $3000 balance in Saving account."
    
class Incorrect_Amount_Error(Exception):
    def __str__(self):
        return f"You must provide positive number for amount to be deposited."
    
class Overdraft_Limit_Error(Exception):
    def __str__(self):
        return f"Overdraft Limit exceeded. You can only use $2000 from overdraft."