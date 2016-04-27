'''
CP1200 Practical 06 Solutions

Created on 11/02/2014

@author: Lindsay Ward
'''
from random import uniform
from math import pow

# Extension 1 - generating

filename = input("Enter the filename: ")
minimum = float(input("Enter the minimum floating-point number: "))
maximum = float(input("Enter the maximum floating-point number: "))
number = int(input("Enter the number of random floats to generate: "))
 
outputFile = open(filename, 'w')
for i in range(number):
    outputFile.write(str(uniform(minimum, maximum)) + "\n")
outputFile.close()

# Extension 2 - statistics (a-e. f & g left for your challenge (lists & dictionaries)

filename = input("Enter the filename: ")
inputFile = open(filename, 'r')

# read the first line and set min, max, total to the first number
minimum = float(inputFile.readline())
maximum = minimum
total = minimum
product = minimum
count = 1 # assume file has at least one number

# read the other numbers
for line in inputFile:
    number = float(line)
    total += number
    product *= number
    count += 1
    if number < minimum:
        minimum = number
    elif number > maximum: # elif since it can never be both 
        maximum = number
inputFile.close()

print("Total:", total)
print("Minimum:", minimum)
print("Maximum:", maximum)
print("Average:", total / count)
print("Geometric mean:", pow(product, 1/count))


# More Practice

# 1.    Write a program that asks the user for a filename, opens that file and then simply prints how many lines are in the file.
# 2.    Write a program that asks the user for a filename, opens that file and then simply prints whether or not the file has any contents.
# a.    Adjust this to print the number of characters (and then words) in the file if you can figure that out.
# combined
filename = input("Enter the filename: ")
inputFile = open(filename, 'r')
lines = inputFile.readlines()
numberOfLines = len(lines)
numberOfChars = 0
if numberOfLines > 0:
    print("Number of lines:", numberOfLines)
    # using the lines list we already have; otherwise we'd just use len(inputFile.read())
    for line in lines:
        numberOfChars += len(line)
    print("Number of characters:", numberOfChars)
else:
    print("This file is empty (no lines)")
inputFile.close()


# 3.    Write a program that asks the user for a phrase and a filename, opens that file and then searches the file to find a line that is equal to the phrase entered. If it finds it, the program should print what line it was found on; otherwise it should print "Not found".
# a.    Adjust this to find the phrase anywhere in the file, including as part of a line, not the whole line.

filename = input("Enter the filename: ")
phrase = input("Enter phrase to find: ")
inputFile = open(filename, 'r')
lines = inputFile.readlines()
found = False
# using a regular for loop so we know what line number
for i in range(len(lines)):
    if phrase in lines[i]:
        print(phrase, "found on line", i + 1)
        found = True
        break
if not found:
    print("Not found")
