
# Q1
for counter in range(3):
    print("Hello")

'''
SET count to 1
WHILE count less than or equal to 3
    OUTPUT "Hello" to screen
    SET count ot count + 1
ENDWHILE
'''

# Q2
# X is input “Enter a number”
x = input("Enter a number to count to")
x = int(x)
for num in range (0, x):
    print(num)

'''
INPUT lastNumber
SET currentnumber to 0
WHILE currentNumber less than or equal to lastNumber
    OUTPUT currentNumber
    SET number to number + 1
'''

# Q3
names = ["Tom", "Dick", "Harry"]
print("name: ")
for name in names:
    print(name)

'''
SET array to ["Tom", "Dick", "Harry"]
FOR name in array
    OUTPUT name
ENDFOR
'''

#Q4
'''
SET total to 0
SET stop to false
WHILE not stop  
    SET number to INPUT ”Enter a number or say Stop to quit”
    IF number is “Stop”
        SET stop to true
    ELSE
        total += number
        OUTPUT total
    ENDIF
ENDWHILE
'''

#Q5
'''
From range (0 to 100)
IF X is divisible by 3
    PRINT 3 squared
X+=3

SET number to 3
WHILE number less than or equal to 100
    COMPUTE number * number as square
    OUTPUT square to screen
    SET number to number + 3
ENDWHILE

SET count to zero
WHILE count is less than or equal to 100
    SET count to count + 1
    IF remainder of count divided by 3 is 0
        OUTPUT count multiplied by count
ENDWHILE
'''

# Q6
'''
Delegates = []
WHILE True:
    Append delegates = input (Add a delegate name or enter 0 to stop)
    IF Delegate is 0:
        BREAK
ENDWHILE

FOR delegate in delegates
    OUTPUT Delegate
ENDFOR

SET delegates to []
WHILE True
    SET newDelegate to input (Add a delegate name or enter 0 to stop)
    IF Delegate is 0:
        BREAK
    SET delegates to delegates + newDelegate
ENDWHILE

FOR delegate in delegates
    OUTPUT Delegate
ENDFOR
'''