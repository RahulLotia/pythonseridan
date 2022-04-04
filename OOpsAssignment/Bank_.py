class Bank:
    _accountList = []
    
    @staticmethod
    def __init__(accounttype):
        Bank._accountList.append(accounttype)
    
    @staticmethod
    def showAll():
        accData = ''
        for account in Bank._accountList:
            accData += f'{account}, {account.__class__.__name__} \n'
        return accData