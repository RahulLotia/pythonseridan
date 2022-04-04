from EmployeeModule import Employee

# Person -> Employee -> ParttimeEmp
#                   |-> FulltimeEmp
#USES
#HAS-A

# PartimeEmp IS-A Employee
class ParttimeEmp(Employee):
    def __init__(self, name: str, address: str, id: str, hourlyPay: float, hours : int = 0, dept: int = 10):
        super().__init__(name, address, id, dept)
        self._hourlyWage = hourlyPay
        self._biweeklyHours = hours

    # def calculateBiweeklyPay(self):
    #     return (self._biweeklyHours * self._hourlyWage)

    def getPay(self):
        return (self._biweeklyHours * self._hourlyWage)

    def __str__(self):
        return f' \n{super().__str__()} Hourly Wage : ${self._hourlyWage} Number of hours worked : {self._biweeklyHours} \
                    Biweekly Pay ${self.getPay():.2f}'
        # return f'{super().__str__()} Hourly Wage : ${self._hourlyWage} Number of hours worked : {self._biweeklyHours} \
        #             Biweekly Pay ${self.calculateBiweeklyPay():.2f}'

    