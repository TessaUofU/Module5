#u0731478 Tessa Price
# Question 2

input_list = [1,2,3,4,[5,6,7,[8,9,[10,[12,13,14,[15,20,25]]]]]]

def locate_inner(input_list):              #Use recursion to access the innermost list of inputlist
    for i in input_list:
        if isinstance(i, list):
            return locate_inner(i)
    return input_list

innermost_list = locate_inner(input_list) #Create a variable with the innermost list to modify it.
recursive_plus= []                         #Create a new list for modified values.

for value in innermost_list:              #Use a for loop to iterate through innermost list and add 1.
    new_value = value + 1
    recursive_plus.append(new_value)

print(recursive_plus)                      #Print new list.
