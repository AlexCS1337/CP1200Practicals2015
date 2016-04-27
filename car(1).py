"""
Solution for Practical 9 - Classes
"""
class Car:
    def __init__(self, fuel):
        """ initialise a Car instance (constructor)
        fuel should be a floating-point number - one unit of fuel drives one kilometre """
        self._fuel = fuel
        self._odometer = 0

    def __str__(self):
        """ string method - for printing a car object """ 
        return "The car has " + str(self._fuel) + " units of fuel and has driven " + str(self._odometer) + "km"
    
    def getFuel(self):
        """ return how much fuel the car has left """
        return self._fuel

    def addFuel(self, amount):
        """ add amount to the car's fuel """
        self._fuel += amount

    def getOdometer(self):
        """ return the odometer reading for the car (i.e. how far it has driven) """
        return self._odometer

    def drive(self, distance):
        """ drive the car a given distance, if it has enough fuel
        if it does not have enough, drive until fuel runs out
        return distance actually travelled """
        if distance > self._fuel:
            distance = self._fuel            
            self._fuel = 0
        else:
            self._fuel -= distance
        self._odometer += distance
        return distance
    