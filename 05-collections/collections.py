# instantiate a list with our first names
# add Bertrand Russell to the end
# change each element to our full names
# remove Bertrand Russell from the list

names = ["Erik", "Daniel", "Alan"]
# copy original list
# one way is to copy the ref only
names2 = names

print(names)

# names.append("Bertrand Russell")#function, requires ()
names2.append("Bertrand Russell")#function, requires ()

print(names)

names[0] += " de Greef"#re-assignment, no ()
names[1] += " Hayter"
names[2] += " Lavender"

print(names)

del names[3]

print(names)

# thoughts:
# the list object is MUTABLE
# think of "Save" on a Word doc
# we can change it in place

# strings, numbers, and booleans are IMMUTABLE
# think of "Save As" on a Word doc
# they cannot be changed in place
# merely a new one created
# and the ref to the old one updated

str1 = "Russell"
str2 = str1
str2 = 'Bertrand Russell'
print(str1)#still containes only Russell
# the difference between strings and lists is NOT in the way we copy them
# it is because
# strings are IMMUTABLE
# lists are MUTABLE