from ClassAModule import ClassA

#single inheritance - only one parent class
class ClassC(ClassA):
    def __init__(self):
        super().__init__()
        self._j1 = 201

    def changeMembers(self):
        self._j1 *= 10

    def commonMethod(self):
        print(f'CommonMethod() from class C')

    def __str__(self):
        return f'{super().__str__()} j1 = {self._j1}'