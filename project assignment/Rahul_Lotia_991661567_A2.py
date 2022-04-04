from pangram import ispangram
from string_encrypt import string_encrypt
from intersection import intersection
from even_number_position import get_index



def runApp(choice):
    choice = 6
    while True!=6:
        print('*************************************')
        print("1 : Check Pangram String")
        print("2 : List of positions of even numbers")
        print("3 : Encrypt the String")
        print("4 : Intersection of lists")
        print("0 : Exit")
        print('*************************************')
        print('\n')
        choice=int(input("Enter your choice : "))
        print('\n')
        if choice == 1:
            string = input('Please Enter a String : ')
            if(ispangram(string) == True):
                print("Given input string is a pangram string",end= ' ')
                print('\n')
            else:
                print("Given input string is not a pangram string",end= ' ')
                print('\n')

        elif choice == 2:
            li = [5, 10, 3, 14, 8, 11, 20, 71, 42, 62]
            get_index(li)

        elif choice == 3:
            s = input('Please Enter a String : ')
            print(string_encrypt(s)+'\n')

        elif choice == 4:
            lst1 = [5, 10, 3, 14, 8, 11, 20, 71, 42, 62]
            lst2 = [2, 14, 31, 15, 28, 10, 20, 11, 28, 62]
            print(f'List 1 = {lst1} \n')
            print(f'List 2 = {lst2} \n')
            print(intersection(lst1, lst2))

        elif choice == 0:
            print("Exiting Program \n")
            break
        else:
            print("Invalid choice \n")
            


runApp(6)