'''
CP1200 Practical 08 Solutions - Lists

Created on 11/02/2014

@author: Lindsay Ward
'''

# Prac 8 Extension Questions
"""
Write a function, memberwiseAddition, that takes two lists, and returns the list that contains 
the sum of elements that are in the same index in the two lists. 
For example
    memberwiseAddition([1, 2, 3], [4, 5, 6]) would return [5, 7, 9] 
    memberwiseAddition([1, 2, 3], [1, 2, 3, 4]) would return [2, 4, 6, 4]
"""
def memberwiseAddition(list1, list2):
    if len(list1) > len(list2):
        longer = list1 # aliasing - OK
        shorter = list2
    else:   # it doesn't matter if they're the same length
        longer = list2
        shorter = list1
    result = longer[:]
    for i in range(len(shorter)):
        result[i] += longer[i]
    return result
                   
# print(memberwiseAddition([1, 2, 3], [1, 2, 3, 4])) 
# a = [1, 2, 3]
# b = [4, 5, 6]
# print(memberwiseAddition(a, b))
# print(a)
# print(b)

"""
2. Extend the first quick question so that the user can enter any number of numbers until a number less
than zero is entered. Adjust the prompt so that it prints like "Number 1: " then "Number 2: " 
"""
numbers = []
i = 1
number = int(input("Number " + str(i) + ": "))
while number >= 0:
    numbers.append(number)
    i += 1
    number = int(input("Number " + str(i) + ": "))
         
print("The first number is", numbers[0])
print("The last number is", numbers[-1])
print("The smallest number is", min(numbers))
print("The largest number is", max(numbers))
print("The average of the numbers is", sum(numbers) / len(numbers))


"""
3.    Write a program that asks the user for an indefinite set of strings (until an empty string is entered), 
then print all of the strings that were repeated (once). 
"""
def findRepeats(items):
    itemsSoFar = []
    repeats = []
    for item in items:
        if item in itemsSoFar: # it's a repeated string
            if item not in repeats: # only store it once
                repeats.append(item)
        itemsSoFar.append(item)
    return repeats

def printStrings(strings, sep):
    for string in strings[:-1]:
        print(string + sep, end=" ")
    print(strings[-1])


items = []
item = input("Please enter a string; empty string to stop: ")
while item:
    items.append(item)
    item = input("Please enter a string; empty string to stop: ")

repeated = findRepeats(items)

if repeated:
    print("Strings repeated: ", end="")
    printStrings(repeated, ",")
else:
    print("No repeated strings entered")
