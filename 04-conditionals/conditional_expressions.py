'''
• IF Temp > 20 THEN
•   OUTPUT "It's warm" to stdout
• ELSE
•   OUTPUT "It's cool" to stdout
• ENDIF
'''
temp = 36
clothing = "T-shirt"
if temp > 20 and temp <= 35:
    print("it's warm")
elif temp > 35:
    print("why did we book this holiday?")
else:
    print("it's cool")

# you could have separate if statements
if temp > 20:
    print("it's warm")

if temp > 35:
    print("pack a", clothing)

    # in this scenario BOTH statements execute
# better to chain with IF - ELIF - ELSE
# then only ONE statement will execute
# there is NO LIMIT to the number of ELIF statements
# modern Python now has an equivalent to Java/JavaScript SWITCH
# this MAY be more performant over larger datasets 

#  there is also a further expression in Java/JavaScript called the TERNARY operator
# again, Python has no equivalent even now
# the Pyhonesque way of doing this 
# is to write an IF-ELSE on one line

light = 0
if light == 0:
    light_switch_state = "off"
else:
    light_switch_state = "on"

light_switch_state = "off" if light == 0 else "on"

print(light_switch_state)
# this forces a hard exclusive OR - one way or the other

is_logged_in = True
user_name = "Alan"
html = f"<p>Welcome {user_name}</p>" if is_logged_in else "<p>Welcome guest</p>"
print(html)