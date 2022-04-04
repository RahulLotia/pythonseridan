
#declaration and definition of the class
from select import select
from productModule import Product

class Application:
    def __init__(self):
        self.productList = []   #empty product list

        # newProduct = Product()
        # newProduct.id = 101
        # newProduct.name = "Watch"
        # newProduct.price = 89.90

        newProduct = Product(101, "Watch", 89.90)
        self.productList.append(newProduct)

        # newProduct = Product()
        # newProduct.id = 102
        # newProduct.name = "Wallet"
        # newProduct.price = 58.99

        newProduct = Product(102, "Wallet", 58.99)
        self.productList.append(newProduct)

        # newProduct = Product()
        # newProduct.id = 103
        # newProduct.name = "Card"
        # newProduct.price = 8.99

        newProduct = Product(103, "Card", 8.99)
        self.productList.append(newProduct)

    def readProductInfo(self):
        idInput = int(input("Enter product ID : "))
        nameInput = input("Enter product name : ")
        priceInput = float(input("Enter product price : "))

        self.productList.append(Product(idInput, nameInput, priceInput))

        # newProduct = Product()
        # newProduct.id = idInput
        # newProduct.name = nameInput
        # newProduct.price = priceInput
        # self.productList.append(newProduct)

    def displayProdList(self):
        if (len(self.productList) == 0):
            print("There are no products in the list at the moment")
        else:
            for prod in self.productList:
                prod.toString()

    def editProduct(self):
        if (len(self.productList) == 0):
            print("There are no products in the list at the moment")
        else:
            idToBeSearched = int(input("Please enter the ID for the product to be edited : "))

            for prod in self.productList:
                if (prod.id == idToBeSearched):
                    #ask for updated info
                    nameInput = input("Enter updated product name : ")
                    priceInput = float(input("Enter updated product price : "))

                    prod.name = nameInput
                    prod.price = priceInput
                    prod.toString()
                    break
            else:
                print(f'The product with {idToBeSearched} doesn\'t exist in the list')

    def searchProduct(self):
        if (len(self.productList) == 0):
            print("There are no products in the list at the moment")
        else:
            idToBeSearched = int(input("Please enter the ID for the product to be searched : "))

            for prod in self.productList:
                if (prod.id == idToBeSearched):
                    prod.toString()
                    break
            else:
                print(f'The product with {idToBeSearched} doesn\'t exist in the list')

            #end of for loop

    def deleteProduct(self):
        if (len(self.productList) == 0):
            print("There are no products in the list at the moment")
        else:
            idToBeSearched = int(input("Please enter the ID for the product to be deleted : "))

            for prod in self.productList:
                if (prod.id == idToBeSearched):
                    # prod.toString()
                    self.productList.remove(prod)
                    #delete the product
                    print(f'The product with ID {idToBeSearched} deleted from the list the list')
                    break
            else:
                print(f'The product with {idToBeSearched} doesn\'t exist in the list')

                
    def runApp(self):
        choice = 0
        while choice != 6:
            print("1 : Add Product")
            print("2 : Edit Product")
            print("3 : Search Product")
            print("4 : Delete Product")
            print("5 : Display Product List")
            print("6 : Exit")
            choice = int(input("Enter your choice : "))
            if choice == 1:
                self.readProductInfo()
            elif choice == 2:
                self.editProduct()
            elif choice == 3:
                self.searchProduct()
            elif choice == 4:
                self.deleteProduct()
            elif choice == 5:
                self.displayProdList()
            elif choice == 6:
                print("Exiting program")
            else:
                print("Invalid choice")

    # def runApp(self):
    #     print("Running the application")
    #     #create the object
    #     prod1 = Product()   #call the initializer
    #     print("before gathering product details")
    #     prod1.toString()

    #     prod1.name = "Tablet"
    #     prod1.id = 987
    #     prod1.price = 657.99
    #     print("after gathering product details and assigning them to object")
    #     prod1.toString()

#create an object to use the class - instance of class
prog = Application()

#using object to call the function using dot (.) operator 
prog.runApp()



# #object is a variable of type Class (Application)
# firstTournament = Application()
# #self keyword in runApp() function will represent firstTournament object; 
# # so that it has access to its (firstTournament object's) attributes and operation
# firstTournament.runApp()

# secondTournament = Application()
# #self keyword in runApp() function will represent secondTournament object; 
# # so that it has access to its (secondTournament object's) attributes and operation
# secondTournament.runApp()

# thirdTournament = Application()
# #self keyword in runApp() function will represent thirdTournament object; 
# # so that it has access to its (thirdTournaments object's) attributes and operation
# thirdTournament.runApp()