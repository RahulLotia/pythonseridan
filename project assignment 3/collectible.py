import os

class CollectibleManager:
    S_FILE_NAME = "CollectibleDB.txt"

    def __init__(self):
        pass

    @staticmethod
    def addCollectible():
        try:
            cID = int(input("Enter Collectible ID : "))
            cName = input("Enter Collectible Name : ")
            cPrice = float(input("Enter Estimated price : "))

            collectibleFile = open(CollectibleManager.S_FILE_NAME, "a") 

            collectibleFile.write(f'{cID},{cName},{cPrice}\n')

        except ValueError as ve:
            print(f'Please provide correct values : {ve}')
        except FileNotFoundError as fnf:
            print(f'File not found at the mentioned location : {fnf}')
        except IOError as ioe:
            print(f'Trouble reading/writing from/to file : {ioe}')
        except:
            print('Something went wrong. Sorry for incovenience.')
        finally:
            collectibleFile.close()        

    @staticmethod
    def editCollectible():
        CollectibleManager.displayCollectible()
        

        try:
            collectibleFile = open(CollectibleManager.S_FILE_NAME, "r")
            fileToWrite = open("TempDB.txt", "a")

            allcollectible = collectibleFile.readlines()

            if len(allcollectible) > 0:
                idToEdit = int(input("Enter Collectible ID to edit : "))

                found = False

                for eachCollectible in allcollectible:
                    attributes = eachCollectible.split(',')

                    if ( idToEdit == int(attributes[0])):
                        print(f'Current Collectible information : {attributes[0]} --- {attributes[1]} --- {attributes[2]}')
                        updatedName = input("Enter updated name : ")
                        updatedPrice = float(input("Enter updated Estimated price : "))                        
                        fileToWrite.write(f'{attributes[0]},{updatedName},{updatedPrice}\n')

                        found = True
                    else:
                        fileToWrite.write(eachCollectible)

                if found != True :
                    print("No matching Collectible found in the database.")
            else:
                print("There are no Collectible in file to edit")


        except FileNotFoundError as fnf:
            print(f'File not found at the mentioned location : {fnf}')
        except IOError as ioe:
            print(f'Trouble reading/writing from/to file : {ioe}')
        except:
            print('Something went wrong. Sorry for incovenience.')
        finally:
            collectibleFile.close()
            os.remove(f'{os.getcwd()}/{CollectibleManager.S_FILE_NAME}')
            os.rename(f'{os.getcwd()}/TempDB.txt', f'{os.getcwd()}/{CollectibleManager.S_FILE_NAME}')

            

    @staticmethod
    def searchCollectible():
        nameToSearch = input("Enter the name of the Collectible to be searched : ")

        try:
            collectibleFile = open(CollectibleManager.S_FILE_NAME, "r")
            allcollectible = collectibleFile.readlines()

            if len(allcollectible) > 0:

                found = False

                for eachCollectible in allcollectible:
                    attributes = eachCollectible.split(',')

                    if ( nameToSearch.upper() == attributes[1].upper()):
                        print(f'{attributes[0]} --- {attributes[1]} --- {attributes[2]}')
                        found = True

                if found != True :
                    print("No matching Collectible found in the database.")
            else:
                print("There are no Collectible in file")


        except FileNotFoundError as fnf:
            print(f'File not found at the mentioned location : {fnf}')
        except IOError as ioe:
            print(f'Trouble reading/writing from/to file : {ioe}')
        except:
            print('Something went wrong. Sorry for incovenience.')
        finally:
            collectibleFile.close()

    @staticmethod
    def deleteCollectible():
        CollectibleManager.displayCollectible()
        
        try:
            collectibleFile = open(CollectibleManager.S_FILE_NAME, "r")
            fileToWrite = open("TempDB.txt", "a")

            allcollectible = collectibleFile.readlines()

            if len(allcollectible) > 0:
                idToDelete = int(input("Enter Collectible ID to delete : "))

                found = False

                for eachcollectible in allcollectible:
                    attributes = eachcollectible.split(',')

                    if ( idToDelete == int(attributes[0])):
                        print(f'Product to delete : {attributes[0]} --- {attributes[1]} --- {attributes[2]}') 
                        found = True
                    else:
                        fileToWrite.write(eachcollectible)

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
            collectibleFile.close()
            os.remove(f'{os.getcwd()}/{CollectibleManager.S_FILE_NAME}')
            os.rename(f'{os.getcwd()}/TempDB.txt', f'{os.getcwd()}/{CollectibleManager.S_FILE_NAME}')


    @staticmethod
    def displayCollectible():
        try:
            collectibleFile = open(CollectibleManager.S_FILE_NAME, "r")

            allCollectible = collectibleFile.readlines()

            if len(allCollectible) > 0:
                for eachCollectible in allCollectible:
                    collectibleAttributes = eachCollectible.split(',')
                    print(f'{collectibleAttributes[0]} --- {collectibleAttributes[1]} --- {collectibleAttributes[2]}')
                    id = int(collectibleAttributes[0])
                    name = collectibleAttributes[1]
                    price = float(collectibleAttributes[2])

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
            collectibleFile.close()

