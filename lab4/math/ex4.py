from math import *
length=float(input("Length of base: "))
height=float(input("Height of parallelogram: "))
def area(length, height):
    return length*height
area_t=area(length,height)
print("Expected Output: ",area_t)
