class Student:
    def __init__(self, id, name):
        self.__id = id
        self.__name = name

    def setID(self, id):
        self.__id = id

    def getID(self):
        return self.__id

    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def toString(self):
        print(f'Student ID = {self.__id} Name = {self.__name}')

    #operator overloading
    def __eq__(self, anotherStudent) -> bool:
        if (self.getID()  == anotherStudent.getID()):
            return True
        else:
            return False
