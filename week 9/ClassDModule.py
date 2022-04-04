from ClassBModule import ClassB
from ClassCModule import ClassC

#multiple inheritance - multiple parent classes
class ClassD(ClassB, ClassC):
    def __init__(self):
        super().__init__()
        self._m1 = 200

    def changeMembers(self):
        super().changeMembers()
        self._m1 *= 5

    def commonMethod(self):
        super().commonMethod()
        print(f'CommonMethod() from class D')

    def __str__(self):
        return f'{super().__str__()} m1 = {self._m1}'