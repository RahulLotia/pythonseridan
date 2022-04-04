from LibraryModule import Library
from BookModule import Book
from FulltimeEmployeeModule import FulltimeEmp
from ParttimeEmployeeModule import ParttimeEmp
from EmployeeModule import Employee

class Employer:
    def __init__(self, employerName : str, library : Library):
        self._employerName = employerName
        # Employer HAS-A Library
        self._library = library

        #alternate
        # initialBookList = [ 
        #     Book("The Silent Spring", "M. Collins", "Non-Fiction"), 
        #     Book("The Alchemist", "P. Coelho", "Fiction"), 
        #     Book("The Orange Sky", "P. Anna.", "Biography") 
        # ]
        # self._library = Library("The scared space", initialBookList)

        #Employer HAS-A Employees
        self._employeeList = [
            FulltimeEmp("Dave", "Montreal", "FT201", 90500.00, 0, dept=30),
            FulltimeEmp("Moi", "Ottawa", "FT301", 43500.00, 2),
            FulltimeEmp("Jamie", "Toronto", "FT598", 78300.00, 1, dept=20),
            ParttimeEmp("Donie", "Hamilton", "PT384", 65.0, 80),
            ParttimeEmp("Fenny", "Brampton", "PT434", 23.0, 65, 20),
            ParttimeEmp("Travis", "Oakville", "PT574", 45.89, 40, 25)
        ]

    def addBookToLibrary(self, book : Book):
        self._library._bookList.append(book)

    def addNewEmployee(self, newEmp : Employee):
        self._employeeList.append(newEmp)

    def getEmployeeList(self):
        return self._employeeList

    def __str__(self):
        outputString = f'Employer : {self._employerName} \nLibrary : {self._library} \nEmployee List : '

        for emp in self._employeeList:
            outputString += f'{emp}'

        return outputString