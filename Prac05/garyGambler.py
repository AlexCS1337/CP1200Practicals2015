__author__ = 'Smoo'


import random

ROULETTE_MINIMUM = 0
ROULETTE_MAXIMUM = 36
ROULETTE_PAYOUT = 36
LUCKY_NUMBER = 18
BET_AMOUNT = 1
MINUTES_PER_SPIN = 1
INITIAL_CASH = 50
TARGET_CASH = 1000
cash = INITIAL_CASH
minutesWasted = 0

while cash > 0 and cash < TARGET_CASH:
    cash -= BET_AMOUNT
    minutesWasted += MINUTES_PER_SPIN

    #write the code to calculate the random roulette spin
    spinNumber = random.randint(ROULETTE_MINIMUM, ROULETTE_MAXIMUM)

    #write the code to add ROULETTE_PAYOUT to cash when LUCKY_NUMBER
    #comes up
    if spinNumber == LUCKY_NUMBER:
        cash += ROULETTE_PAYOUT

    #display how much cash Gary has right now
    print("Cash = $", cash, sep="")

if cash <= 0:
    print("Garry, you have lost $", INITIAL_CASH, ".", sep="")
    #calculate hours wasted, and minutes left over
    # e.g. 33 hours and 51 minutes
    hoursWasted = minutesWasted // 60
    minutesLeftOver = minutesWasted % 60
    print ("You have also wasted", hoursWasted, "hours and", \
           minutesLeftOver, "minutes!")
else:
    print("You got lucky this time. But in the end, every gambler loses.")
