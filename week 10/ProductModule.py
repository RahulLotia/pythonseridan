import os

class ProductManager:
    # class variable or static variables
    S_FILE_NAME = "ProductDB.txt"

    def __init__(self):
        pass

    @staticmethod
    def addProduct():
        try:
            #ask user to input product info
            pID = int(input("Enter product ID : "))
            pName = input("Enter product Name : ")
            pPrice = float(input("Enter product price : "))

            #open a file to write data 
            productFile = open(ProductManager.S_FILE_NAME, "a")   #a = append data
            # productFile = open(ProductManager.S_FILE_NAME, "w") #w = write data

            #if file successfully opened, write the data in CSV format to file 
            # pID,pName,pPrice
            productFile.write(f'{pID},{pName},{pPrice}\n')

        except ValueError as ve:
            print(f'Please provide correct values : {ve}')
        except FileNotFoundError as fnf:
            print(f'File not found at the mentioned location : {fnf}')
        except IOError as ioe:
            print(f'Trouble reading/writing from/to file : {ioe}')
        except:
            print('Something went wrong. Sorry for incovenience.')
        finally:
            productFile.close()
        

    @staticmethod
    def editProduct():
        ProductManager.displayProduct()
        

        try:
            productFile = open(ProductManager.S_FILE_NAME, "r")
            fileToWrite = open("TempDB.txt", "a")

            allProducts = productFile.readlines()

            if len(allProducts) > 0:
                idToEdit = int(input("Enter product ID to edit : "))

                found = False

                for eachProduct in allProducts:
                    attributes = eachProduct.split(',')

                    if ( idToEdit == int(attributes[0])):
                        print(f'Current product information : {attributes[0]} --- {attributes[1]} --- {attributes[2]}')
                        updatedName = input("Enter updated name : ")
                        updatedPrice = float(input("Enter updated price : "))
                        # f'{attributes[0]},{updatedName},{updatedPrice}'

                        # open the file for writing
                        
                        fileToWrite.write(f'{attributes[0]},{updatedName},{updatedPrice}\n')

                        found = True
                    else:
                        fileToWrite.write(eachProduct)

                if found != True :
                    print("No matching product found in the database.")
            else:
                print("There are no products in file to edit")


        except FileNotFoundError as fnf:
            print(f'File not found at the mentioned location : {fnf}')
        except IOError as ioe:
            print(f'Trouble reading/writing from/to file : {ioe}')
        except:
            print('Something went wrong. Sorry for incovenience.')
        finally:
            productFile.close()

            #delete original file ProductDB.txt
            # "path/ProductDB.txt"
            # os.getcwd() -> return Current Working Directory (cwd) path
            os.remove(f'{os.getcwd()}/{ProductManager.S_FILE_NAME}')

            #rename the temporary file TempDB.txt to ProductDB.txt to make it original with updated records
            os.rename(f'{os.getcwd()}/TempDB.txt', f'{os.getcwd()}/{ProductManager.S_FILE_NAME}')

            



    @staticmethod
    def searchProduct():
        nameToSearch = input("Enter the name of the product to be searched : ")

        try:
            productFile = open(ProductManager.S_FILE_NAME, "r")
            allProducts = productFile.readlines()

            if len(allProducts) > 0:

                found = False

                for eachProduct in allProducts:
                    attributes = eachProduct.split(',')

                    if ( nameToSearch.upper() == attributes[1].upper()):
                        print(f'{attributes[0]} --- {attributes[1]} --- {attributes[2]}')
                        found = True

                if found != True :
                    print("No matching product found in the database.")
            else:
                print("There are no products in file")


        except FileNotFoundError as fnf:
            print(f'File not found at the mentioned location : {fnf}')
        except IOError as ioe:
            print(f'Trouble reading/writing from/to file : {ioe}')
        except:
            print('Something went wrong. Sorry for incovenience.')
        finally:
            productFile.close()

    @staticmethod
    def deleteProduct():
        ProductManager.displayProduct()
        
        try:
            productFile = open(ProductManager.S_FILE_NAME, "r")
            fileToWrite = open("TempDB.txt", "a")

            allProducts = productFile.readlines()

            if len(allProducts) > 0:
                idToDelete = int(input("Enter product ID to delete : "))

                found = False

                for eachProduct in allProducts:
                    attributes = eachProduct.split(',')

                    if ( idToDelete == int(attributes[0])):
                        print(f'Product to delete : {attributes[0]} --- {attributes[1]} --- {attributes[2]}') 
                        found = True
                    else:
                        fileToWrite.write(eachProduct)

                if found != True :
                    print("No matching product found in the database.")
            else:
                print("There are no products in file to delete")


        except FileNotFoundError as fnf:
            print(f'File not found at the mentioned location : {fnf}')
        except IOError as ioe:
            print(f'Trouble reading/writing from/to file : {ioe}')
        except:
            print('Something went wrong. Sorry for incovenience.')
        finally:
            productFile.close()

            #delete original file ProductDB.txt
            # "path/ProductDB.txt"
            # os.getcwd() -> return Current Working Directory (cwd) path
            os.remove(f'{os.getcwd()}/{ProductManager.S_FILE_NAME}')

            #rename the temporary file TempDB.txt to ProductDB.txt to make it original with updated records
            os.rename(f'{os.getcwd()}/TempDB.txt', f'{os.getcwd()}/{ProductManager.S_FILE_NAME}')


    @staticmethod
    def displayProduct():
        try:
            productFile = open(ProductManager.S_FILE_NAME, "r") #r = read from file

            #read all lines from the file
            #readlines() will return a list containing all lines as individual element of list
            allProducts = productFile.readlines()

            if len(allProducts) > 0:
                #TODO iterate through the list to access individual products
                for eachProduct in allProducts:
                    #extract individual attributes from one record
                    productAttributes = eachProduct.split(',') #will return list
                    print(f'{productAttributes[0]} --- {productAttributes[1]} --- {productAttributes[2]}')
                    #you need to convert the values you read from file from string to respective data types
                    #reading from file always gives string data
                    id = int(productAttributes[0])
                    name = productAttributes[1]
                    price = float(productAttributes[2])

                    # print(f'Discounted ($1) price for {name} is ${price - 1}')
            else:
                print("There are no products in the file")
        except TypeError as te:
            print(f'Upsupported data types for the operation : {te}')
        except FileNotFoundError as fnf:
            print(f'File not found at the mentioned location : {fnf}')
        except IOError as ioe:
            print(f'Trouble reading/writing from/to file : {ioe}')
        except:
            print('Something went wrong. Sorry for incovenience.')
        finally:
            productFile.close()

