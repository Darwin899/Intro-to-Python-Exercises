print("Enter 10 integers")
v = []
for i in range(10):
    x = int(input())
    v.append(x)

# Duplicates are removed
s = set()
for i in v:
    # Set will not accept duplicates
    s.add(i) 

# Print unique elements as list
print(list(s)) 