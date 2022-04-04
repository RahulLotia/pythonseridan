import string
from unittest import result


num1 =10
num2 =20

sum = num1 + num2

# using f-string
print(f'Sum is {sum}')

print('sum is ', sum, 'num1', num1, 'num2', num2)

#num1 = int(input("Enter Number 1 = "))
#num2 = int(input("Enter Number 2 = "))

#print(f'type of num1{type(num1)} Type of num2 {type(num2)}')

#print(f'Sum of {num1} and {num2} is {num1 + num2}')

result = 10/5
result = 10.5/5.2       # this will give you long answer
result = 10.5//5.2      #"//" is used only for int part of the fraction
result = 30 % 5         # modulo answer
print(f'result is {result}')


c1 = True
c2 = False

print(f'c1 and c2 {c1 or c2} {c1 & c2}') #logical AND
print(f'c1 and c2 {c1 or c2} {c1 | c2}') #logical OR


#binary
num3 = 0b10101 #for binary will be 0b
print(f'int of num3 is {num3}')
print(f'binary of a given number 34 {bin(34)}') #'bin' is for getting binary number of the given number
print(f'number of bits in a given number 54 in binary = {int(56).bit_length()}')

#for short hand expressions

result = 0
result += 10
result *=20
#result /=50

if result >50:
    print(f'result = {result} is greater then 50')
else:
    print(f'result = {result} is less then 50')

