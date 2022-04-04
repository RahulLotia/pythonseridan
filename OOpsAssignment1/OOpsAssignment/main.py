from Account_Exceptions import *
from Bank_ import Bank
from ChequingAccounts import ChequingAccount
from SavingAccount import SavingsAccount


Bank._accountList.append(SavingsAccount("S101\t", "James Finch\t", "222210212\t", 3400.90))
Bank._accountList.append(SavingsAccount("S102\t", "Kell Forest\t","222214500\t", 42520.32))
Bank._accountList.append(SavingsAccount("S103\t", "Amy Stone\t","222212000\t", 8273.45))
Bank._accountList.append(ChequingAccount("C104\t", "Kaitlin Ross\t","333315002\t", 91230.45))
Bank._accountList.append(ChequingAccount("C105\t", "Adem First\t","333303019\t", 43987.67))
Bank._accountList.append(ChequingAccount("C106\t", "John Doe\t","333358927\t", 34829.76))


def run():
    print(f'{ "-" * 25} All Account Information { "-" * 25}')
    print(f'ConsumerID\tName\tAccountNo\tBalance\tType\t')
    print(f'{ "-" * 25} All Account Information { "-" * 25}')
    print(Bank.showAll())
    Bank._accountList.append(SavingsAccount("S647\t", "Alex Du\t", "222290192\t", 4783.98))
    Bank._accountList.append(ChequingAccount("C576\t", "Dale Stayne\t", "333312312\t", 12894.56))
    print(f'{ "-" * 90}')
    print(f'Trying to withdraw $500.00 from the following account')
    print(Bank._accountList[0].__str__()+ '  ' + Bank._accountList[0].__class__.__name__)
    try :
        Bank._accountList[0].withdraw(500.00)
    
    except Minimum_Balance_Error:
        print('You must maintain minimum $3000 balance in Saving account.')

    print(f'{ "-" * 90}')
    print(f'{ "-" * 90}')
    print(f'Trying to deposit $-250.00 to the following account')
    print(Bank._accountList[1].__str__() + '  ' + Bank._accountList[1].__class__.__name__)
    try :
        Bank._accountList[1].deposit(-250.00)
    except Incorrect_Amount_Error:
        print('You must provide positive number for amount to be deposited.')

    print(f'{ "-" * 90}')
    print(f'{ "-" * 90}')
    print(f'Trying to withdraw $10000.00 to the following account')
    print(Bank._accountList[2].__str__()+ '  ' + Bank._accountList[2].__class__.__name__)
    try: 
        Bank._accountList[2].withdraw(10000.00)
    except Insufficent_Balance_Error:
        print('Insufficient balance in the account. Cannot withdraw.')

    print(f'{ "-" * 90}')
    print(f'{ "-" * 90}')
    print(f'Trying to deposit $5000.00 to the following account')
    print(Bank._accountList[2].__str__()+ '  ' + Bank._accountList[2].__class__.__name__)
    Bank._accountList[2].deposit(5000.00)
    print(f'{ "-" * 90}')
    print(f'{ "-" * 90}')
    print(f'Trying to deposit $7300.00 to the following account')
    print(Bank._accountList[3].__str__()+ '  ' + Bank._accountList[3].__class__.__name__)
    Bank._accountList[3].deposit(7300.00)
    print(f'{ "-" * 90}')
    print(f'{ "-" * 90}')
    print(f'Trying to withdraw $45000.40 from the following account')
    print(Bank._accountList[4].__str__()+ '  ' + Bank._accountList[4].__class__.__name__)
    try :
        Bank._accountList[4].withdraw(45000.40)

    except Insufficent_Balance_Error:
        print('Insufficient balance in the account. Cannot withdraw.')

    print(f'{ "-" * 90}')
    print(f'{ "-" * 90}')
    print(f'Trying to withdraw $37000.00 from the following account')
    print(Bank._accountList[5].__str__()+ '  ' + Bank._accountList[5].__class__.__name__)
    try :
        Bank._accountList[5].withdraw(37000.00)
    except Overdraft_Limit_Error:
        print('Overdraft Limit exceeded. You can only use $2000 from overdraft.')
    print(f'{ "-" * 90}')
    print(f'{ "-" * 25} All Account Information { "-" * 25}')
    print(f'ConsumerID\tName\tAccountNo\tBalance\t\tType\t ')
    print(f'{ "-" * 25} All Account Information { "-" * 25}')
    print(Bank.showAll())

run()