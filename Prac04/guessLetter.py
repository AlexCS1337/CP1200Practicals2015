__author__ = 'Smoo'


# for x in "hello":
#     print(x * 2, end="")

count = 1
SECRET = 'a'
guess = input("Guess the letter: ")
while len(guess) != 1:
    print("Invalid length guess. Enter one letter.")
    guess = input("Guess the letter: ")
while guess != SECRET:
    print("That's not it.")
    count += 1
    guess = input("Guess the letter: ")
print ("You got it!")
print ("It took you", count, "times.")