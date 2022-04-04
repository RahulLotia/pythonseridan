from ClassAModule import ClassA

class ClassB(ClassA):
    def __init__(self):
        super().__init__()
        self.k1 = 101
        self._k2 = 102
        self.__k3 = 103

    def setK3(self, num):
        self.__k3 = num
    
    def getK3(self):
        return self.__k3

    def changeNumber(self):
        # super().changeMembers()
        self.k1 += 10
        self._k2 += 10
        self.__k3 += 10
        self.n1 += 10
        self._n2 += 10
        # self.__n3 += 10
        self.setN3(self.getN3() + 10)

    def commonMethod(self):
        print(f'CommonMethod() from class B')

    def __str__(self):
        return f'{super().__str__()} k1 = {self.k1} k2 = {self._k2} k3 = {self.__k3}'
