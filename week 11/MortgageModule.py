class Mortgage:
    def __init__(self, housePrice = 0.0, term = 1, rate = 0.0, downPer = 0):
        self.__housePrice = housePrice
        self.__term = term
        self.__rate = rate
        self.__downPaymentPer = downPer

    def setHousePrice(self, price):
        self.__housePrice = price

    def setTerm(self, term):
        self.__term = term

    def setRate(self, rate):
        self.__rate = rate

    def setDownpayemt(self, down):
        self.__downPaymentPer = down

    def getHousePrice(self):
        return self.__housePrice

    def getTerm(self):
        return self.__term

    def getRate(self):
        return self.__rate

    def getDownPer(self):
        return self.__downPaymentPer

    def getMonthlyMortgage(self):
        dwnAmount = (self.__housePrice * self.__downPaymentPer / 100)
        p = self.__housePrice - dwnAmount
        r = self.__rate / 100 / 12
        n = self.__term * 12

        return ( p * (r * pow(1+r, n)) / (pow(1+r, n) - 1) )

    def __str__(self):
        return f'House Price : $ {self.__housePrice} \n Term : {self.__term} years \n \
        Rate of Interest : {self.__rate} % \n Down Payment : {self.__downPaymentPer} % \n \
            Monthly Mortgage Amount : $ {self.getMonthlyMortgage()} '