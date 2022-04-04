from collectible import CollectibleManager

class Application:
    def optionlist(self, operation):
        if operation == 1:
            print("Adding new Collectible")
            CollectibleManager.addCollectible()
        elif operation == 2:
            print("Editing Collectible")
            CollectibleManager.editCollectible()
        elif operation == 3:
            print("Searching for Collectible")
            CollectibleManager.searchCollectible()
        elif operation == 4:
            print("Deleting Collectible")
            CollectibleManager.deleteCollectible()
        elif operation == 5:
            print("Displaying all Collectibles")
            CollectibleManager.displayCollectible()
        elif operation == 6:
            print("Clossing the Appliction. GoodBye!")
        else:
            print("Please enter valid choice.")

    def run(self):

        choice = 0

        while choice != 6:
            print("-"*50)
            print("1 : Add Collectible")
            print("2 : Edit Collectible")
            print("3 : Search Collectible")
            print("4 : Delete Collectible")
            print("5 : Display Collectible List")
            print("6 : Exit")
            print("-"*50)

            while True:
                try:
                    choice = int(input("Enter your choice : "))
                except ValueError as ve:
                    print(f'Please enter valid number [1-6]. Try again ! {ve}')
                else:
                    self.optionlist(choice)
                    break

    


app = Application()
app.run()