from ProductModule import ProductManager

class Application:
    def doMenuOperations(self, operation):
        if operation == 1:
            #TODO add new product and save it to file
            print("Adding new product")
            ProductManager.addProduct()
        elif operation == 2:
            #TODO edit product info and save it to file
            print("Editing product")
            ProductManager.editProduct()
        elif operation == 3:
            #TODO search for product from the file
            print("Searching for product")
            ProductManager.searchProduct()
        elif operation == 4:
            #TODO delete product from the file
            print("Deleting product")
            ProductManager.deleteProduct()
        elif operation == 5:
            #TODO display all products' info from the file
            print("Displaying all products")
            ProductManager.displayProduct()
        elif operation == 6:
            print("Terminating the program. Bye!")
        else:
            print("Please enter valid choice.")

    def run(self):

        # newProduct = ProductManager()

        choice = 0

        while choice != 6:
            print("-"*50)
            print("1 : Add Product")
            print("2 : Edit Product")
            print("3 : Search Product")
            print("4 : Delete Product")
            print("5 : Display Product List")
            print("6 : Exit")
            print("-"*50)

            while True:
                try:
                    choice = int(input("Enter your choice : "))
                    # break

                    # self.doMenuOperations(choice)
                    # break
                except ValueError as ve:
                    print(f'Please enter valid number [1-6]. Try again ! {ve}')
                else:
                    self.doMenuOperations(choice)
                    break

    


app = Application()
app.run()