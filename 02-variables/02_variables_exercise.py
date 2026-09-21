# suppose we want to capture number input from the user
# in order to coerce the datatype to int or float 
# we have to re-assign using int() or float()

# in order to output the data with a string
# we need to coerce numbers AGAIN back to strings
# is there an easier way - YES

number = input("enter your account number")
balance = input("enter the balance you wish to transfer")
number = int(number)
balance = float(balance)

print("Account number; ", number)
print("Account balance; ", balance)
# print("Account number; "+ number)#TypeError: can only concatenate str (not "int") to str
# print("Account balance; "+ balance)
print("Account number; "+ str(number))#works
print("Account balance; "+ str(balance))

# since Python 3.7 inline placeholders take ANY data OR expression 
# and concatenate it in a string
print(f"Account number: {number}, Account balance: €{balance * 103 / 100}")