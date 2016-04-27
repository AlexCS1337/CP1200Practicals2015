__author__ = 'Smoo'


# Fictiontorial

def fictiontorial(n):
    if n <= 0:
        return 0
    else:
        fictiontorial(n) / fictiontorial(n -1)

fictiontorial(4)


# Pyramid Planning

getRows = input("Number or rows: ")
