#Iteration Statements
#Loops

#Conditional Loop

count = 0

while count <= 10 :
    print(count)
    count += 1  #count = count + 1

print(f'loop completed count = {count}')


#Infinite loop - because value of count variable is not updated
#use ctrl + C to stop the infinite execution

# count = 1
# while count < 5:
#     print(count)
    

#Infinite loop - because value of count variable is decremented instead of incrementation

# 1-2-3-4
# count = 1
# while count < 5:
#     print(count)
#     count -= 1  #this statement should add 1 to count
    # 1 -> 0 -> -1 -> -2 -> ....

# print("Another while loop completed")

num1 = 10
num2 = 15

while num1 < num2:
    print(f'num1 {num1} num2 {num2}')
    # num1 += 2
    num2 -= 2

print("Loop 3 terminated")

#counted loop

#0, 1, 2, 3, 4
#iteration variable
for n in range(5):
    print(f'n = {n}')

print("Loop 4 terminated")   

for name in ["Abira", "Daniel", "Dawood", "Mariam", "Radhika", "Parth", "Tauheed"] :
    # print(name, sep = "---")
    print(name, end = "---")

print("Loop 5 terminated") 

#for interation_variable in sequence :
for ch in "The Message" :
    print(ch)

print("Loop 6 terminated")

msg = "The Output Message"

for ch in msg[2:9]:
    print(ch, end = " -- ")

print("Loop 7 terminated")

print(f'range(5) {range(5, 10)}')

# for n in range(5,10) :
# for n in range(1 ,10, 2) :
for n in range(15, 5, -1) :
    print(n , end = " -- ")


print()
numbers = [2, 4, 9, 13, 17, 21, 82, 92]     #list
for n in numbers:
    print(n, end = " -- ")
print()

for _ in range(3):
    print("Good Morning")

#0, 1, 2, 3, 4, 5, 6
for day in range(7):
    if day == 0:
        # print("It's holiday")
        print(f'Day {day} It\'s holiday')  # \ is used to escape from special meaning of ' (Single quote)
    elif day >= 1 and day <=5:
        print("It's a work day")
    else:
        print("Saturday is family day")

numbers = range(5)  #0, 1, 2, 3, 4
print(numbers)

for n in [0, 2, 4, 5, 8, 11, 12]:
    if n % 2 != 0:
        # continue
        break

    print(f'n = {n}')

print("Loop terminated")

# logical error
# count = 1
# while count <= 10:

#     if count % 2 != 0:
#         continue

#     print(f'count = {count}')
#     count += 1

for day in range(7):
    if day >= 1 and day <= 5:
        continue

    print("Let's Party")

#nested loops
for row in range(5):    #outer loop
    print(f'row = {row}')

    for col in ["a", "b", "c"] :    #inner loop
        print(col, end = " == ")

    print()

print()
print("nested loops end")

result = pow(2, 3)
print("result = ", result)

lines = 4
for row in range(lines):

    # print(" ", end = " ")
    for col in range(row+1):
        print("#", end = " ")

    print()