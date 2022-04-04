#List - Collection of multiple values of same data type

#create empty list
classList = []

#initialize values to list
classList = ["Anchal", "Haniya", "Hatim", "Nour"]

#create List with initial values
members = ["Parth", "Shreya", "Deni", "Tim"]

print(f'classList : {classList}')
print(f'members : {members}')
print(f'type of members : {type(members)}')
print(f'number of members : {len(members)}')

numbers = [12, 56, 9, 29, 1, 87, 34, 72, 0, -3, 72, 85]

sum = 0
for n in numbers:
    sum += n # sum = sum + n #shorthand operator

print(f' sum of numbers : {sum}')

#append()

for n in numbers[3 : 8]:
    print(n, end = "-")

print()

# print(f'fifth member : {members[4]}')   #IndexError
print(f'fourth member : {members[3]}')

for count in range(len(numbers)):
    print(numbers[count])

print("display numbers in reverse")
#range(start, end, direction)
for count in range(len(numbers)-1, -1, -1):
    print(numbers[count], end = "-")

print()
print(numbers[4])

#append a new element at the end of list
members.append("Rahul")
members.append("Hyder")
members.append("Manpreet")

print(members)

numbers.append(65)

# while True:
#     name = input("Enter member name [enter 'STOP' to finish] : ")

#     if name.upper() == 'STOP':
#         break;
#     else:
#         members.append(name)        

# print(members)

# while True:
#     num = int(input("Enter number [enter 0 to stop] : "))

#     if num == 0:
#         break;
#     else:
#         numbers.append(num)   

# print(numbers)

print(members)
members.remove("Tim")
print(members)
members.insert(3, "Tony")
print(members)
members.pop(2)
print(members)
members.sort()
print(members)
members.reverse()
print(members)

numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)
print(max(numbers))
print(min(numbers))


if "Tim" in members:
    members.remove("Tim")
    print("Tim removed from members list")
else:
    print("Tim is not in members list")

if "Parth" not in members:
    members.append("Parth")
    print("Parth was not present in the members list..just appended")
else:
    print(f'Parth is already in the members list at index {members.index("Parth")}')


#Strings
day = "Wednesday IS woRk    IS        Day"
print(day.upper())
print(day.lower())
print(day.swapcase())
print(day.capitalize())
print(day.count('e'))
print(day.find("is")) #-1 not present #index otherwise
print(day.find("IS")) #index 10

words = day.split() #whitespaces - tab, space, newline
print(words)

words = day.split('a')
print(words)

decorator = '-*-Hello---' * 50
print(decorator)

decorator += " The End "
print(decorator)

password = "ItsMe@1012"
valid = False

if (len(password) < 6):
    print("Invalid password. Must contain at least 6 characters")
else:
    for ch in password:
        #there could be multiple conditions in varioud different order of execution to match different password rules
        if ch.isdigit() or ch.isalnum() or ch.islower() or ch.isupper():
            valid = True
        else:
            valid = False

    if valid:
        print("Password is valid")
    else:
        print("Invalid password")

