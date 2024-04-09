from math import *
n=int(input("Input number of sides:"))
s=float(input("Input the length of a side:"))
def area(n,s):
    return (1/4)*n*s**2*(1 / tan(pi / n))
polynomal_area=area(n,s)
print(f"The area of the polygon is:, {polynomal_area:.2f}")