
#global variable
x = 1

print(f'first time x = {x}')

def print_number():
    num1 = 20   #local variable - available only in method scope
    print(f'value of x within function = {x}')
    print(f'num1 * 3 = {num1 * 3}')    

#calling the print_number() function
print_number()

print(f'second time x = {x}')

#Name Error - cannot access local variable/method variable outside the method
#print(f'num1 * 3 = {num1 * 3}')

#parent scope
for outer in [1,2,3,4,5]:
    print(f'outer  = {outer}')

    for inner in ['a', 'b', 'c', 'd']:
        print(f'inner = {inner} @ out = {outer}', end = " - ")  #child scope

    print()
    print(f'Inner for loop ends after {inner}')


print(f'outer after both loops end = {outer}')
print(f'inner after both loops end = {inner}')

def outerMethod():
    a1 = 1

    def innerMethod():
        a2 = 2
        print(f'a1 within inner {a1}')
        print(f'a2 within inner {a2}')

    print(f'a1 within outer {a1}')
    #NameError - a2 is declared within inner scope which means it is not available in outer scope
    # print(f'a2 within outer {a2}')
    innerMethod()  

#most outer scope
outerMethod()

#NameError - innerMethod() is declared within inner scope which means it is not available in outer scope
# innerMethod()