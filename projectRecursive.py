""" Lindsay Ward, 02/04/10 - 20/03/14, CP1200 Project Solutions 

- Recursive string-printing (outside-in) question

Write a program that prints a string from the outside in, using recursion.
E.g. if the string to print is "Programming", your program should print: "P g r n o i g m r m a".

Remember to analyse and design this problem first. Think about the base and recursive cases - when will it stop (base) and how will it reduce the problem (recursive) each time?

Base case: when string is empty or one character
Recursive: the string minus the first and last character

Pseudocode:
function main()
    get string
    printOutIn(string)

function printOutIn(string)
    if length of string is 0
        return
    else if length of string is 1
        print string
        return
    print first and last character of string
    printOutIn(string[1:-1]
        
    
"""

def main():
    inString = input("Enter a string: ")
    printOutIn(inString)
    print()
    if isPalindrome(inString):
        print(inString, "is a palindrome")
    else:
        print(inString, "is not a palindrome")

    numRows = int(input("Enter number of rows for 2D pyramid: "))
    print(blocks2D(numRows), "blocks are required for", numRows, "rows.")

def printOutIn(string):
    if len(string) == 0:
        return
    elif len(string) == 1:
        print(string, end=" ")
        return
    print(string[0], string[-1], end=" ")
    printOutIn(string[1:-1])

""" Write a recursive function to determine if a string is a palindrome
    (e.g. hannah is a palindrome, but han is not).
"""
def isPalindrome(string):
    """ Extension question - returns true if a string is a palindrome, false otherwise """
    # True if the string is 0 or 1 characters long
    if len(string) == 0 or len(string) == 1:
        return True
    # True if the outside characters match, and the rest of it is a palindrome
    if string[0].upper() == string[-1].upper():
        return isPalindrome(string[1:-1])
    else:
        return False

""" Determine the number of blocks required for a 2D pyramid of a given height in rows (n) 
"""
def blocks2D(n):
    if n == 1:
        return 1
    return n + blocks2D(n-1)

main()
        
