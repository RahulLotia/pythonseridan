from math import factorial
from MethodsModule import Methods
from StudeneModule import Student

class Application:
    def run(self):
        obj1 = Methods()

        # obj1.printInfo("Patel", "Jigisha") #incorrect positions
        # obj1.printInfo(3, "Jigisha") #incorrect types
        # obj1.printInfo("Jigisha") #required argument missing
        obj1.printInfo("Jigisha", "Patel")

        obj1.printAge("John", 19)
        # obj1.printAge(age = 19, address = "Toronto")  #error
        # obj1.printAge()   #error
        obj1.printAge("Carter", "Toronto")
        # obj1.printAge(19, "John")

        #keyword arguments
        obj1.printAge(name = "Ted", address = "Oakville")

        obj1.printAge(name = "Moi", age = 30, address = "Oakville")
        obj1.printAge(address = "Markham", name = "Mili", age = 28 )
        # obj1.printAge("Markham","Mili", 28 )

        # sum1 = obj1.calculateSum(10, 20, "JK") #error
        sum1 = obj1.calculateSum(10, 20, name = "JK")
        print(f'sum1 / 4 = {sum1/4}')

        sum2 = obj1.calculateSum(10, 45, 30, 40, name = "PK")
        print(f'sum2 = {sum2}')

        sum3 = obj1.calculateSum(10, 2098, 30, 40, 50, 70, 980, 90, name = "MK")
        print(f'sum3 = {sum3}')

        groceryList = ["Apples", "Veggies", "Milk", "Dish Soap"]
        print(f'Grocery list before function call : {groceryList}')
        obj1.alterList(groceryList) #pass the variable by reference
        print(f'Grocery list after function call : {groceryList}')

        #collections are sent as reference to methods
        #individual arguments/variableas are sent as values to methods
        n1 = 20
        print(f'n1 before call : {n1}')
        obj1.alterNumber(n1)
        print(f'n1 after call : {n1}')

        # print(f'myList = {myList}')   #error

        fact = factorial(10)
        print(f'factorial(10) = {fact}')

        # obj1.printData(2000)
        Methods.printData(2000)

        # obj2 = Methods()
        # obj2._number = 20
        Methods.printData(5000)

        stud1 = Student(101, "JK")
        stud1.toString()

        stud2 = Student(102, "Jimmy")
        stud2.toString()

        stud3 = Student(101, "James")
        stud3.toString()

        if (stud1 == stud3):
            print(f'Both are the same students')
        else:
            print(f'Both students are DIFFERENT')

       

app = Application()
app.run()