# Declaring a list
arr1=[]
i = 0
# Prompts user to enter a number or "QUIT"
l = input("Enter a number or QUIT to quit: ")
while (l != "QUIT"):
    arr1.append(int(l))
    l = input("Enter a number or QUIT to quit: ")

# Declaring a second list 
arr2=[]
# This method makes sure only the even numbers from list "arr1" can go into list "arr2"
for i in range(0, len(arr1)):
    if(arr1[i] % 2 == 0):
        arr2.append(arr1[i])

# Use print method to print list "arr2"        
print(arr2)