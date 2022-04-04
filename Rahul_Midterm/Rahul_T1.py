



def runApp():
        name=(input("Enter Name : "))
        age=int(input("Enter Age : "))
    
        if age >= 25:
            speed=input("Have You ever had a speeding ticket Y/N : ")
            if speed == "y" or speed == "Y":
                print("Your Premium Amount will be $1000")
            elif speed == "n" or speed == "n":
                print("Your Premium Amount will be $500")
        elif age < 25:
            speed=input("Have You ever had a speeding ticket Y/N : ")
            drivingcourse= input("Have you ever taken a driving Course Y/N : ")
            if speed == "y" or speed == "Y":
                if drivingcourse == "y" or drivingcourse=="Y":
                    print("Your Premium Amount will be $1500")
                elif drivingcourse=="n" or drivingcourse =="N":
                    print("You are not Eligible")
            elif speed == "n" or speed == "n" and drivingcourse=="y":
                print("Your Premium Amount will be $1000")
        quote=input("Do you want to add a person Y or N :")
        if quote=="y" or quote=="Y":
            runApp()

runApp()
