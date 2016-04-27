__author__ = 'Smoo'

import circle
import rectangle

width = float(input("Enter the width of the rectangle: "))
height = float(input("Enter the height of the rectangle: "))

rectangleArea = rectangle.calculateArea(width, height)
rectanglePerimeter = rectangle.calculatePerimeter(width, height)

print("The area of a rectangle is", rectangleArea, "and the perimeter of a rectangle is", rectanglePerimeter)

radius = float(input("Enter the radius of the circle: "))

circleArea = circle.calculateArea(radius)
circleCircumference = circle.calculateCircumference(radius)

print("The area of a circle is", circleArea)
print("The circumference of a circle is", circleCircumference)

