"""Write a python program which accepts the radius of circle from user and
compute the area."""
import math
radius = float(input("Enter the radius of the circle: "))

area = math.pi * radius**2

print(f"The area of the circle is: {area:.1f}")