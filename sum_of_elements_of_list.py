n1 = int(input('Enter first element:'))
n2 = int(input('Enter second element:'))
n3 = int(input('Enter third element:'))
num_list = [n1, n2, n3]


def sum(num):
    total = 0
    for index in num:
        total += index
    return total


ans = sum(num_list)
print('sum of elements is', ans)
