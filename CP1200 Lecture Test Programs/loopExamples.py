__author__ = 'Smoo'

# While Loop - Count down from 10 then prints Blast Off
#
# number = 10
# while number >= 0:
# 	print(number)
# 	number = number - 1
# print("Blast off!")

# Asks user to guess a number
#
# SECRECT_NUMBER = 6
# number = int(input("? "))
# while number != SECRECT_NUMBER:
#     print("Guess again!")
#     number = int(input("? "))
# print("You got it!")

#
# print(list(range(10)))

#
# for i in range(3):
#     print("Hello")

#
# numbers = (13, 4, -1, 0, 9, 123, 55)
#
# total = 0
# for number in numbers:
#     total += number
# print(total)

#
# Prints the total of ages and the average
#
total = 0
count = 0
age = int(input("Type in an age: "))
while age != -1:
    total += age
    count += 1
    age = int(input("Type in an age: "))
if count != 0:
    print("total", total)
    print("average", total / count)
else:
    print("no total or average")

#
# startYear = int(input("Start "))
# endYear = int(input("End "))
#
# for year in range(startYear, endYear, 4):
#     print(year)
