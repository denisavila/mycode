#!/usr/bin/env python3
print('Basic Calculator')
print('You need to provide a,b and operation')
print('')
print('1 : +')
print('2 : -')
print('3 : *')
print('4: /')
print('5 : a^b')
#print('What operation do you want?')
#print('What operation do you want?')

a = float(input('Enter value for a: '))
b = float(input('Enter value for b: '))

operation = int(input('Operation: 1,2,3,4,5? '))

if operation == 1:
    message = a + b
elif operation  == 2:
    message = a - b
elif operation == 3:
    message = a * b
elif operation == 4:
    message = a / b
elif operation == 5:
    message = a ** b
else:
    message = "select a valid operation 1,2,3,4,5"

print(message)
