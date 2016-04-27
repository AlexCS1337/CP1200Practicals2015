__author__ = 'Smoo'

# outFile = open("name.txt", "w")
# name = input("What is your name?: ")
# outFile.write(name)
# outFile.close()

# inFile = open("name.txt", "r")
# name = inFile.read().strip()
# print("Your name is", name)
# inFile.close()

inFile = open("numbers.txt", "r")
total = 0
for line in inFile:
    number = int(line.strip())
    total += number
print(total)
inFile.close()