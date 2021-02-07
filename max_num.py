#function to find maximum number
n1= int(input('Enter 1st number:'))
n2= int(input('Enter 2nd number:'))
n3= int(input('Enter 3rd number:'))
def max(a,b,c):
    if a>b and a>c:
        print(a,'is the largest number')
    elif b>a and b>c:
        print(b, 'is the largest number')
    else:
        print(c, 'is the largest number')

max(n1,n2,n3)