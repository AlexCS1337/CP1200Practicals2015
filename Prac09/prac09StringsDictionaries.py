'''
CP1200 Practical 09 Solutions - Strings

Created on 11/02/2014
Modified   01/05/2014

@author: Lindsay Ward
'''

# Operations on Strings

# string = input("Enter a string: ")
string = "banana split"
reversed = ""
for i in range(len(string) - 1, -1, -1):
    reversed += string[i]
print("1.", reversed)

print("2.", string[0:3])

print("3.", string.replace('a', ''))

print("4.", string.upper())

# we can use the reversed string we already have
print("5.", reversed[0:3].upper())

spacedString = ""
for letter in string:
    spacedString += letter + " "
print("6.", spacedString)

print("7.", end=" ")
words = string.split(sep=" ")
for i in range(len(words) - 1, -1, -1):
    print(words[i], end=" ")
print()


# File line adder-upper

def main():
    filename = input("Enter the filename: ")
    fileIn = open(filename, 'r')
    i = 1
    for line in fileIn:
        total = addUpLine(line)
        print("Total for line ", i, " is ", total, ".", sep="")
    fileIn.close()

def addUpLine(line):
    # split the line into parts
    parts = line.split(",")
    # add up all the parts
    total = 0
    for number in parts:
        total += int(number)
    # return the total
    return total

# main()

# Dictionary Warm-up
# Write a program that uses a constant dictionary (use ALL_CAPS) to store the Australian state abbreviations and names - e.g. QLD is Queensland. Then ask the user for their 'short' state and print the full state name.
STATE_NAMES = {"QLD":"Queensland", "NSW": "New South Wales", "NT":"Northrern Territory", "WA":"Western Australia", "ACT":"Australian Capital Territory", "VIC":"Victoria","TAS":"Tasmania"}
# print(STATE_NAMES)

state = input("Enter short state: ").upper()
while state != "":
    if state in STATE_NAMES:
        print(state, "is", STATE_NAMES[state])
    else:
        print("Invalid short state")
    state = input("Enter short state: ").upper()



# Autocorrector Program
# Note that this solution has a problem because it ignores punctuation
# E.g. "lyk!" will not get corrected to "like!" because "lyk!" is the 'word' that split produces.
# Fixing that issue is beyond the scope of this exercise.

inputFile = open("misspellings.txt", 'r')
correctionsDict = {}
for line in inputFile: # we know the format of each line
    parts = line.strip().split(",")
    correctionsDict[parts[0]] = parts[1]
inputFile.close()
# print(correctionsDict) # left in here to show you the process - build the dictionary and test (print) it to see it works before moving on

text = input("Enter a line of text to correct: ")
while text != "":
    words = text.split(" ")
    correctedText = ""
    for word in words:
        if word in correctionsDict: # checks keys only
            correctedText += correctionsDict[word]
        else:
            correctedText += word
        correctedText += " "
    print("You should have written:", correctedText)
    text = input("Enter a line of text to correct: ")

print("Go forth and spell correctly!")

exit()

# Word Counter
filename = input("Enter the filename: ")
inputFile = open(filename, 'r')
# initialise a dictionary of unique words
uniqueWords = {}

# Add the unique words in the file to the list
for line in inputFile:
    words = line.split()
    for word in words:
        freq = uniqueWords.get(word, None)
        if freq == None:
            uniqueWords[word] = 1
        else:
            uniqueWords[word] = freq + 1

# Print the unique words and their frequencies,
# in alphabetical order
words = list(uniqueWords.keys())
words.sort()
for word in words:
    print(word, ":", uniqueWords[word])

inputFile.close()
