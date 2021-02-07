def up_lower(line):
    up = 0
    lower = 0
    for c in line:
        if c.isupper():
            up += 1
            print('Upper case letters:', up)
        elif c.islower():
            lower += 1
            print('Lower case letters:', lower)
        else:
            print('pass')


up_lower('Quick Brown Fox')
