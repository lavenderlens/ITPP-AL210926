# int

my_number = 42      #initialisation - first time the variable pops up in code
print(isinstance(my_number, int))#True
print(my_number.is_integer())#True
print(type(my_number))#<class 'int'>

#float
my_number = 42.0      #re-assignment
print(isinstance(my_number, float))#True
print(type(my_number))#<class 'float'>

#complex
my_number = 1 + 1j#real and imaginary parts
# used for things like calculating the square root of a negative number
print(type(my_number))#<class 'complex'>

# boolean
my_boolean = True
print(type(my_boolean))#<class 'bool'>

#string
my_string = "Hello"
print(type(my_string))#<class 'str'>

# the container types hold multiple values, referenced by one variable
numbers = [1,2,3]
# lists are the first types of collection you will learn
# they are ordered, indexed, and permit duplicates
# they have a length prop
print(len(numbers))#3
print(type(numbers))#<class 'list'>
print(numbers[0])#1
print(numbers[2])#3
# print(numbers[3])#IndexError: list index out of range

print("Strings are indexed too")
print(len(my_string))
print(my_string[0])

#None
my_none = None
print(type(my_none))#<class 'NoneType'>
# Python equivalent to null
# used for de-referencing variables of other types
# effectively erasing/resetting
my_string = None
# print(my_string[0])#TypeError: 'NoneType' object is not subscriptable


