# reading from standard input
# the input() function builtin returns a string object
# if necessary we will have to convert this to other datatypes

print("enter a number:")
num1 = input()
print(num1)
print(type(num1))

# num2 = int(input("enter another number"))#not best practice for exception handling
num2 = input("enter another number")
print(type(num2))

print(num1 + num2)

num1 = float(num1)
print(type(num1))#<class 'int'>
num2 = float(num2)
print(num1 + num2)
