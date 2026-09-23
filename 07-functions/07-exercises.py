# Q1
def my_function():
    print("This is my function")
    print("Hello")
 
my_function()

# Q2
def print_sum(numbers):
    sum = 0
    for num in numbers:
        sum += num
    print(sum)

print_sum([1,2,3])

def print_product(number1, number2):
    # result = number1 * number2
    # print(result)
    print(number1 * number2)
    # return number1 * number2

# run Q2
num1 = input("Please input your first number")
num2 = input("Please input your second number")
num1 = int(num1)
num2 = int(num2)
operation = input("Please input 1 for sum or 2 for product")
if operation == "1":
    print_sum(num1, num2)
elif operation == "2":
    print_product(num1, num2)
else:
    print("ERROR")


# Q3
def get_average(numbers):
    total = 0
    length = 0
    for number in numbers:
        total += number
        length += 1
    average = total / length
    return average

def get_average_refactored(numbers):
    # total = 0
    # length = 0
    # for number in numbers:
    #     total += number
        # length += 1
    # average = total / length
    # average = total / len(numbers)
    # return average
    return sum(numbers) / len(numbers)
