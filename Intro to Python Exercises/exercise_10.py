# Prompting User to Enter string
string = (input("Enter the string\n")) 
# Breaking string variable into list of characters
lst = list(string) 

# Printing list of characters
print("List of character is: ")
print(lst) 

# Assigning number of element in each list
x = 3 
print("New list of list is :")

# Using list comprehension to create list of list
A = [lst[i:i + x] for i in range(0, len(lst), x)]
print(A)