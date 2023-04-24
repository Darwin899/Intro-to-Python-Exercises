# Asks user to type in a grade number
grade = int(input("Enter a grade from 0-100: ")) 

if grade >= 90:
    print("A")
elif grade >= 80:
    print("B")
elif grade >= 70:
    print("C")
elif grade >= 60:
    print("D")
else:
    # If grade is anyhting below 60 "F" gets printed
    print("F") 