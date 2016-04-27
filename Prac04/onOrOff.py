__author__ = 'Smoo'


onOrOff = input("Enter either on or off: ")
while onOrOff != "on" and onOrOff != "off":
    print("Invalid choice, try again.")
    onOrOff = input("Enter either on or off: ")
if onOrOff == "on":
    print("the light is on")
elif onOrOff == "off":
    print("the light is off")