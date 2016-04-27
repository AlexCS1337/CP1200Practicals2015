"""
CP1200 Practical 09 - Autocorrect - to complete
Created by Trevor Andersen, 2013
"""

def main():
    correctionsDict = buildCorrectionsDict("corrections.txt")
    lineToCorrect = input("Enter a line of text to correct: ")

    while lineToCorrect != "":
        correctedLine = getCorrectedText(lineToCorrect, correctionsDict)
        print("You should have written:", correctedLine)
        lineToCorrect = input("Enter a line of text to correct: ")

    print("Go forth and spell correctly!")
    
def buildCorrectionsDict(filename):
    fileIn = open(filename, 'r')
    result = {}
    
    for line in fileIn:
        # GET THE INCORRECT AND CORRECT WORDS FROM THE LINE
        # PUT THE WORDS IN THE DICTIONARY (INCORRECT to CORRECT)

    fileIn.close()
    return result

def getCorrectedText(text, correctionsDict):
    result = text

    for incorrectWord in correctionsDict:
        # GET THE CORRECT WORD FROM THE DICTIONARY
        # REPLACE THE INCORRECT WORD WITH THE CORRECT ONE (USE .replace)

    return result

main()
        
        
