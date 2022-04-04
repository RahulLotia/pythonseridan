
class Product:
    #inbuilt-function to initialize the class variables
    #constructor or initializer
    #called automatically when the object is created
    # def __init__(self):
    #     #attributes
    #     self.id = 0     #int
    #     self.name = "Unknown"   #string
    #     self.price = 0.0    #float

    def __init__(self, pid: int, pname: str, pprice: float):
        #attributes
        self.id = pid
        self.name = pname
        self.price = pprice

    def toString(self):
        #operation / function
        print(f'ID : {self.id} Name : {self.name} Price : {self.price}')