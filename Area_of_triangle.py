
import math

print("                                    This is a program to calculate are of a triangle")
a=int(input("Entre a side of a triangle\n"))
b=int(input("Enter a 2nd side of triangle\n"))
c=int(input("Enter 3rd side of triangle\n"))
s=(a+b+c) /2
print("S is", s)
area1= s*(s-a)*(s-b)*(s-c)
area= math.sqrt(area1)
print("Area of the triangle is :\n" ,area)
