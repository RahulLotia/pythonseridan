from EmployeeModule import Employee

class FulltimeEmp(Employee):
    def __init__(self, name: str, address: str, id: str, annualpay : float, leaves : int = 0, dept: int = 10):
        super().__init__(name, address, id, dept)
        self._annualPay = annualpay
        self._numberOfLeaves = leaves
        # self._biweeklyPay = 0.0

    # def calculatePay(self):
    #     # self._biweeklyPay = self._annualPay / 26
    #     return (self._annualPay / 26)

    #method overrding - polymorphism
    # implement abstract method
    def getPay(self):
        return (self._annualPay / 26)

    #method overrding
    def __str__(self):
        return f' \n{super().__str__()} Annual Pay : ${self._annualPay} Number of Leaves : {self._numberOfLeaves} Biweekly Pay : ${self.getPay():.2f}'

        # return f' {super().__str__()} Annual Pay : ${self._annualPay} Number of Leaves : {self._numberOfLeaves} Biweekly Pay : ${self.calculatePay():.2f}'

