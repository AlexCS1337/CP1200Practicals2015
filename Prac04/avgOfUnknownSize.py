__author__ = 'Smoo'

SENTINEL = -1
totalAge = 0
totalPeople = 0

age = int(input("What is your age? "))
while age != SENTINEL:
    totalAge += age
    totalPeople += 1
    age = int(input("What is your age? "))
print (totalAge)
print (totalPeople)
