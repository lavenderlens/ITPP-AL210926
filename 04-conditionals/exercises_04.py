import random

magicNumber = random.randint(1, 10)
print(magicNumber)#testing

userGuess = input("Please guess a number between 1 and 10: ")
userGuess = int(userGuess)
if userGuess < 1 or userGuess > 10:
    print("please enter a valid number 1-10")
elif userGuess  == magicNumber:
    print("You got it")
elif abs(userGuess - magicNumber) == 1:
    print("so close!)")
else:
    print("Way off!")


age = 21
if age < 18:
    print("you are a minor")
else:
    if age < 65:
        print("you are working age")
    else:
        print("you are retirement")

if age < 18:
    print("you are a minor")
elif age < 65:
    print("you are working age")
else:
    print("you are retirement")

# lists (collection)
cereals = ["shreddies", "cheerios", "honey nut cornflakes"]
print("first cereal", cereals[0])
cereal = input("Enter your choice of cereal")
if cereal.lower() in cereals:
    print("you can have breakfast")
