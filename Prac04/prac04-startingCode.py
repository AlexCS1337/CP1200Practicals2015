'''
CP1200 - Practical 04 - Starting code
'''
def displayOdds():
    maximum = int(input("Enter the maximum value to display: "))
    for i in range(1, maximum + 1, 2):
        print(i, end=' ')

def displayEvens():
    maximum = int(input("Enter the maximum value to display: "))
    for i in range(2, maximum + 1, 2):
        print(i, end=' ')        

def displayReciprocals():
    maximum = int(input("Enter the maximum value whose reciprocal to display: "))
    for i in range(1, maximum + 1):
        print(format(1/i, ".6f"), end=' ')

# display the menu
#<INSERT CODE HERE>
# get the choice
#<INSERT CODE HERE>

while <INSERT CODE HERE>:
    # select between the different options
#    <INSERT CODE HERE>
    # display the menu
#    <REPEAT CODE HERE>
    # get the choice
#    <REPEAT CODE HERE>
