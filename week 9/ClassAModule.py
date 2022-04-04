class ClassA:
    s_num = 1234    #static variable or class variable

    def __init__(self):
        #field variable or instance variable
        self.n1 = 10    #public member - accessible anywhere even outside the package
        self._n2 = 20   #protected member - accessible in child class as well; not accessible outside the package
        self.__n3 = 30  #private variable - only accessible within class ; not accessible in child class

    #mutator/setter method
    def setN3(self, num):
        self.__n3 = num

    #accessor/getter method
    def getN3(self):
        return self.__n3

    @staticmethod
    def changeStaticVariable():
        ClassA.s_num = 1000
        # self.n1 *= 2  cannot access instance variables with static method

    def changeMembers(self):
        self.n1 *= 2    #self.n1 = self.n1 * 2
        self._n2 *= 2
        self.__n3 *= 2

    def commonMethod(self):
        print(f'CommonMethod() from class A')

    def __str__(self):
        return f'n1 = {self.n1} n2 = {self._n2} n3 = {self.__n3}'