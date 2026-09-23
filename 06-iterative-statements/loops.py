print("# for loop with a counter")
for x in range(1,6):#startIndex inclusive, endIndex exclusive
    print(x)

print("# while loop with counter")
counter = 1
while counter < 6:
    print(counter)
    counter += 1
# there are NO for loops at runtime

print("# while loop with collection")
counties = ["Kent", "Surrey", "Suffolk"]
index = 0
while index < len(counties):
    print(counties[index])
    index += 1

print("# for loop with collection")
for county in counties:
    print(county)

print("# break, while loop with a counter")
x = 1
while True:
    if x == 6:
        break
    print(x)
    x += 1

print("# break, for loop with a collection")
for county in counties:
    if county == "Surrey":
        break
    print(county)

print("# break, while loop with a collection")
count = 0
while count < len(counties):
    if counties[count] == "Surrey":
        break
    print(counties[count])
    count += 1

# the break keyword stops looping when i is encountered
# the continue keyword skips one iteration only
print("# continue, for loop with a collection")
for county in counties:
    if county == "Surrey":
        continue
    print(county)

print("# continue, while loop with a collection")
count = 0
while count < len(counties):
    if counties[count] == "Surrey":
        count += 1#must increment also in continue branch
        continue
    print(counties[count])
    count += 1

# BEST scenario for a for loop: a collection
# BEST scenario for a while loop: when the no.of iterations
# is NOT known in advance

guest_list = []
while True:
    name = input("enter a name for the guest list or zero (0)to quit")
    if name == "0":
        break
    guest_list.append(name)

for guest in guest_list:
    print(guest)
([{()}])