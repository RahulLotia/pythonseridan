class Product():
    def __init__(self, name = str , price = float, quantity = 1):
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_cost(self):
        cost = self.quantity * self.price
        return float(cost)

    def toString(self):
        self.cost = self.calculate_cost()
        print(f'Buying {self.quantity} {self.name} at the price of {self.price} in Ontario would cost you $ {self.cost}')
        
    
prod1 = Product("Pen", 2.50, 10)
prod1.toString()

prod2 = Product("Milk", 7.99)
prod2.toString()

prod3 = Product("Apples", 4.99, 2)
prod3.toString()

prod4 = Product("Banana", 17.67, 2)
prod4.toString()