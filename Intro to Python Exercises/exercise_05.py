# Ask user to input 5 integers
print("Enter 5 integers") 
v1 = []
v2 = []
for i in range(5):
    # Typecast the input value to int
    v1.append(int(input())) 

# Ask user to input 5 more integers
print("Enter 5 integers")
for i in range(5):
    # Typecast the input value to int
    v2.append(int(input())) 

# Create new list
v3 = [] 

for i in v1:
    if i in v2:
        v3.append(i)

# Use print method to print the list
print(v3)