# Declare an empty list variable called wordList
wordList = []
for i in range(5):
    # Prompt user to input a word
    word = input("Enter the #{} word: ".format(i+1))
     # Append the word to the wordList
    wordList.append(word)


# Declare and empty variable named wordString
wordString = ""
# Loop the words in the wordList
for word in wordList:
    # Get the first character of each word in the word list and append a space at the end
    singleString = word[:1] + " "
    # Append the singleString to the wordString
    wordString += singleString

# Use the print method to print the wordList and the wordString
print("Words:", wordList)
print("One String:", wordString)