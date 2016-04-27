'''
CP1200 Prac 05 Solutions - Functions
Created on 11/02/2014

@author: Lindsay Ward
'''
from random import randint, uniform

# Min & Max - Part B
def getLimits():
    minimum = int(input("Enter the minimum: "))
    prompt = "Enter the maximum (" + str(minimum) + " or above):"
    maximum = int(input(prompt))
    while maximum < minimum: # maximum must not be less than minimum
        print("Maximum too low!")
        maximum = int(input(prompt))
    return minimum, maximum

# min, max = getLimits()
# print(min, max)


# Extension - Gopher Population Simulator
STARTING_POPULATION = 1000
BIRTH_RATE_MIN = .1
BIRTH_RATE_MAX = .2
DEATH_RATE_MIN = .05
DEATH_RATE_MAX = .25
YEARS_TO_SIMULATE = 10

population = STARTING_POPULATION
print("Welcome to the Gopher Population Simulator!")
print("Starting population:", STARTING_POPULATION)
for year in range(YEARS_TO_SIMULATE):
    # births
    births = round(uniform(BIRTH_RATE_MIN, BIRTH_RATE_MAX) * population)
    deaths = round(uniform(DEATH_RATE_MIN, DEATH_RATE_MAX) * population)
    population = population + births - deaths
    print("\nYear", year + 1, "\n*****")
    print(births, "gophers were born.", deaths, "died.")
    print("Population:", population)

