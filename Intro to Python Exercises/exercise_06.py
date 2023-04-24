# Prompt user to enter row and column number 
row = int(input("Enter a row num from 1 to 5: "))
col = int(input("Enter a col num from 1 to 5: "))
# Loop for rows 
for i in range(1, 6):
    # Loop for column 
    for j in range(1, 6):
        # check condition if it matches 
        if i == row and j == col:
            # print 1
            print("1", end=" ")
        else:
            # print 0
            print("0", end=" ")
    print()
