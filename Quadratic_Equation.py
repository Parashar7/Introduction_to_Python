# program to find the roots of a quadratic equation
import math

a = int(input('Enter the coefficient of x^2:'))
b = int(input('Enter the coefficient of x:'))
c = int(input('Enter the constant value:'))
d = (b * b) - (4 * a * c)
if d >= 0:
    print('Roots are real!!')
    root1 = (-b + math.sqrt(d)) / (2 * a)
    root2 = (-b - math.sqrt(d)) / (2 * a)
    print('Roots are', float(root1), 'and', int(root2))
elif d == 0:
    print('No roots!!')
else:
    print('Roots are imaginary!!')
