num_list=[3,5,2]

def sum(num):
    total=0
    for index in num:
        total+=index
    return total

ans=sum(num_list)
print(ans)
