from functions_module import greet_to, print_all, print_sum, get_sum
# import functions_module

# functions_module.greet_to("Alan", 60)
greet_to("Alan", 60)
# call greet_to the WRONG way
# greet_to(60, "Alan")#TypeError: unsupported operand type(s) for -: 'int' and 'str'
# greet_to("Aln")#TypeError: greet_to() missing 1 required positional argument: 'age'
greet_to(age=60, name="Alan")#named args
# does NOT require equals in definition
greet_to()#values may now be omitted
# BUT if provided, they override the default values

print_all(["Al", "Erik", "Daniel"])
print_all("Python")

print_sum([1,2,3,4])#10
get_sum([1,2,3,4])#nothing
print(get_sum([1,2,3,4]))#10