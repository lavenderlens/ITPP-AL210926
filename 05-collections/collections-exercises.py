'''

peudocode patterns
INPUT
CALCULATE/COMPUTE
OUTPUT

inside that,

IF...ELSE IF...ELSE

FOR

WHILE

1.
a group of things given a group name, which should be a plural noun

2.
Each value has a position or place in the whole, defined by its index
indices start at zero, and increment by one

3.
ArrayName[IndexNumber] = "newValue" #SET
NewVariableName = ArrayName[IndexNumber] #GET

4.
beverages=["Water", "Beer", "Coffee"]
    OUTPUT beverages [1]


SET doors to ["tiger", "tiger","tiger","prize", "tiger"]
INPUT GuessTheDoor from user
IF doors[GuessTheDoor] == "prize"
    OUTPUT "you won the prize"
ELSE
    OUTPUT "you got a tiger"
ENDIF

6
x, y, z coordinates can be represented [0,0,0]
FORWARD: increment z [0,0,1]
LEFT: decrement x [-1,0,1]
UP: increment y [-1, 1, 1]

coordinates = [0 ,0 ,0]
direction = input “Choose to go up, down, left, right, in or out”
IF direction is "up"
              SET Coordinates [1] TO Coordinates [1]+1
ELSEIF direction is down
              Coordinates [1] -1
ELSEIF direction is right
              Coordinates [0] +1
ELSEIF direction is left
              Coordinates [0] -1
ELSEIF direction is out
              Coordinates [2] +1
ELSE direction is in
              Coordinates [2] -1
END IF

'''

'''
SET doors to ["tiger", "tiger","tiger","prize", "tiger"]
INPUT GuessTheDoor from user
IF doors[GuessTheDoor] == "prize"
    OUTPUT "you won the prize"
ELSE
    OUTPUT "you got a tiger"
ENDIF'''

doors = ["tiger", "tiger","tiger","prize", "tiger"]
guess_door = input("Guess the door 1-5 where the prize is")
guess_door = int(guess_door)
if doors[guess_door] == "prize":
    print("You won the prize")
else:
    print("eek it's a tiger!")