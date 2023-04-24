str1 = input('Enter a string: ')
str2 = input('Enter another string: ')

#find length of strings
a = len(str1)
b = len(str2)

#if a is prefix of b
if(a<b and str2[0:a]==str1):
    print("True")

#if b is prefix of a
elif(a>=b and str1[0:b]==str2):
    print("True")

#if no prefix exist
else:
    print("False")
