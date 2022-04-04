

class Methods:
    def __init__(self):
        self._number = 10   #field variable

    #required arguments
    def printInfo(self, fName, lName):
        print(f'Number  = {self._number}')
        print(f'full name is {fName} {lName}')
        print(f'First Name {fName}')
        print(f'Last Name {lName}')
        # print(f'Last Name {lName / 3}')

    #default arguments
    def printAge(self, name, age = 10, address = "Unknown"):
    # def printAge(self, age = 10, address = "Unknown", name): #error
        print(f'name = {name}')
        print(f'Age = {age}')
        print(f'Address = {address}')

    #variable length arguments
    # def calculateSum(self, *numbers):
    def calculateSum(self, *numbers, name):
        #parameters or arguments or local variables
        print(f'argument at index 1 = {numbers[1]}')
        print(f'Called by : {name}')
        sum = 0

        for num in numbers:
            sum += num

        # print(f'sum = {sum}')
        return sum

    def alterList(self, myList):
        #myList = local variable / parameter
        myList.append("Pen")
        print(f'myList within method : {myList}')

    def alterNumber(self, num):
        num = num / 5
        print(f'number within function call : {num}')

    #recursive function
    def factorial(self, n):
        # 5 * 4! (4 * 3! (3 * 2! (2 * 1! (1 * 0!))))
        print(f'Calling factorial({n})')

        if n == 0:
            return 1
        else:
            recurse = self.factorial(n-1)
            result = n * recurse
            return result

    #static method - belong to the class not the object
    @staticmethod
    def printData(data):
        # print(f'number = {self._number}')
        print(f'Applying rule A for tax calculation on {data} income')
        # print(f'this is {data} from static method')