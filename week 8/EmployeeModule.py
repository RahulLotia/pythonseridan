from PersonModule import Person
from abc import ABC, abstractmethod
from BookModule import Book

# Person - super class or base class or parent class
# Employee - sub class or derived class or child class

# Employee IS-A Person
#Inheritance
class Employee(Person):
    def __init__(self, name: str, address : str, id : str, dept: int = 10):
        super().__init__(name, address)
        self._empID = id
        self._dept = dept

    #blueprint - abstract method - child class must implement this method
    #must not contain definition
    @abstractmethod
    def getPay(self):
        pass

    #Employee USES Book
    def takeBreak(self, book : Book):
        print(f'{self._name} reading {book._title}')

    #method overrding
    def __str__(self):
        return (f'{super().__str__()} EmpID : {self._empID} Dept: {self._dept}')