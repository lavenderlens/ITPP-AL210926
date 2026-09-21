'''
input number1
input number2 
compute number1 / number2 = quotient
compute number1 % number2 = remainder
output quotient, remainder
'''

number1 = input("Enter a number")
number1 = int(number1)
number2 = input("Enter a second number")
number2 = int(number2)
quotient = number1 // number2
remainder = number1 % number2
print(quotient, remainder)
