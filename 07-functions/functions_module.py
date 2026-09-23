def greet():
    print("Hello")
    print("How are you?")
print("Carrying on as usual...")
greet()

'''
• def greet(name, age):
• yearOfBirth = 2024 – age
• print("Hello " + name)
• print("You were born in " + str(yearOfBirth))
'''

# def greet_to(name, age):#positional args
def greet_to(name='friend', age=21):#default args
    year_of_birth = 2026 - age
    print(f"Hello {name}")
    print(f"You were born in {year_of_birth}")

'''
• def print_all(array):
• for element in array:
• print(element)
'''
def print_all(list):
    for el in list:
        print(el)

def print_sum(numbers):
    sum = 0
    for num in numbers:
        sum += num
    print(sum)

def get_sum(numbers):
    sum = 0
    for num in numbers:
        sum += num
    return sum