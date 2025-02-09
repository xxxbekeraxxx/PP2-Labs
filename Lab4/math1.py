#Problem 1
import math
degree = float(input("Input degree: "))
radian = math.radians(degree)
print(f"Output radian: {radian:.6f}")

print(" ")

#Problem 2
h = int(input("Enter height:" ))
b1 = int(input("Enter base1 :"))
b2 = int(input("Enter base2: "))
area = (b1 + b2) * h/2
print(f"Area of trapezoid: {area}")

print(" ")
#Problem 3

import math
n = int(input("Input num of sides: "))
s = float(input("Input the lenght of a side: "))

area = (n * s **2)/(4 * math.tan(math.pi / n))
print(f"The area of the palygon is: {area}")

print(" ")

#Problem 4
length = int(input("Length of base: "))
height = int(input("Height of parallelogram:"))
area = length * height
print(f"Expected Output: {area:.1f}")
