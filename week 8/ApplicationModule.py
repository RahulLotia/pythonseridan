from audioop import add
from PersonModule import Person
from EmployeeModule import Employee
from FulltimeEmployeeModule import FulltimeEmp
from ParttimeEmployeeModule import ParttimeEmp
from BookModule import Book
from LibraryModule import Library
from EmployerModule import Employer

class Application:
    def run(self):
        # self.testInheritane()
        # self.testLibrary()
        self.testEmployer()

    def testEmployer(self):
        booksList = [ 
            Book("The Silent Spring", "M. Collins", "Non-Fiction"), 
            Book("The Alchemist", "P. Coelho", "Fiction"), 
            Book("The Orange Sky", "P. Anna.", "Biography") 
        ]

        lib1 = Library("Under the tree", booksList)

        college = Employer("The Study Space", lib1)
        print(college)

        college.addNewEmployee(FulltimeEmp("Angie", "Hamilton", "FT928", 78960.00, 0,))
        college.addNewEmployee(ParttimeEmp("Rony", "Oakville", "PT893", 54, 20, 15))
        print(f' {("-" * 80)} \n {college}')

        college._employeeList[3].takeBreak( Book("The Orange Sky", "P. Anna.", "Biography") )

    def testLibrary(self):
        booksList = [ 
            Book("The Silent Spring", "M. Collins", "Non-Fiction"), 
            Book("The Alchemist", "P. Coelho", "Fiction"), 
            Book("The Orange Sky", "P. Anna.", "Biography") 
        ]

        lib1 = Library("Under the tree", booksList)
        print(lib1)

    def testInheritance(self):
        
        #object of PErson class
        person1 = Person("Jim", "Oakville")
        # person1._name = "Jim"
        # person1._address = "Oakville"
        print(person1.__str__())

        #object of Employee class
        employee1 = Employee("Jack", "Burlington", "E101", 20)
        # employee1._name = "Jack"
        # employee1._address = "Burlington"
        # employee1._empID = "E101"
        # employee1._dept = 20
        print(employee1.__str__())

        employee2 = Employee(address = "Hamilton", id = "E102", name = "Jill")
        print(employee2.__str__())

        ftEmp1 = FulltimeEmp(name = "Tim", address="Hamilton", id= "FT201", annualpay=75000.00, leaves=0, dept=5)
        # ftEmp1.calculatePay()
        print(ftEmp1.__str__())
        print(f'Fulltime employee pay : {ftEmp1.getPay()}')

        ptEmp1 = ParttimeEmp(name = "Shawn", address="Toronto", id= "PT971", hourlyPay=35.89, hours=40)
        # ptEmp1.calculateBiweeklyPay()
        print(ptEmp1.__str__())
        print(f'Parttime employee pay : {ptEmp1.getPay()}')


app = Application()
app.run()