#Filehandling exercises:
#1.Write a Python program to count the number of lines in a text file.

# Opening a file
file = open("test.txt","r")
Counter = 0
  
# Reading from file
Content = file.read()
CoList = Content.split("\n")
  
for i in CoList:
    if i:
        Counter += 1
          
print("This is the number of lines in the file")
print(Counter)

#2.find the longest words.


def longest_word(filename):
    with open(filename, 'r') as infile:
              words = infile.read().split()
    max_len = len(max(words, key=len))
    return [word for word in words if len(word) == max_len]

print(longest_word('testfile.txt'))



#3.Print the number of distinct words and number of occurrences in txt file
# Open the file in read mode
text = open("sample.txt", "r")
  
# Create an empty dictionary
d = dict()
  
# Loop through each line of the file
for line in text:
    # Remove the leading spaces and newline character
    line = line.strip()
  
    # Convert the characters in line to 
    # lowercase to avoid case mismatch
    line = line.lower()
  
    # Split the line into words
    words = line.split(" ")
  
    # Iterate over each word in line
    for word in words:
        # Check if the word is already in dictionary
        if word in d:
            # Increment count of word by 1
            d[word] = d[word] + 1
        else:
            # Add the word to dictionary with count 1
            d[word] = 1
  
# Print the contents of dictionary
for key in list(d.keys()):
    print(key, ":", d[key])
