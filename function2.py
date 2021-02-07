#function to sqaure a nnumber

n= int(input("Enter a number to be squared:"))
n1= int(input("Enter a number to be cubed:"))
def sq(num,num1,expression):
    print(expression)
    sq_num= num*num
    sq1_num= num1*num1*num1
    print(expression)
    return sq_num, sq1_num

ans= sq(n,n1,'good')

print(ans)

#n1= int(input("Enter a number to be cubed:"))
#def sq1(num1):
    #sq1_num= num1*num1
    #return sq1_num

#ans1= sq1(n1)
#print(ans1)
