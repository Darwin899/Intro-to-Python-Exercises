n = int(input("Enter a number: "))
# declaring a list 
numbers = [] 

for i in range(n):
    # appends to the next value given by the user
    numbers.append(int(input("Enter number: "))) 

numbers.sort()

# check if the list has an even or odd number of elements
if n % 2 == 0:
    median = (numbers[n//2 - 1] + numbers[n//2]) / 2
else:
    median = numbers[n//2]

# Use the print method to print the numbers
print("List:", numbers)
# Use the print method to print the median
print("Median:", median)