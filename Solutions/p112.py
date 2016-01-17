def bouncy(n):
    """
    input: integer n
    output: boolean True/False
    return True if number is bouncy
    e.g. is not increaing or decreasing order digits
    1232, 155349 etc
    """
    flag1 = False
    flag2 = False
    temp = str(n)
    for idx in range(1, len(temp)):
        if not temp[idx] <= temp[idx - 1]:
            flag1 = True
            break
    for idx in range(len(temp) - 1):
        if not temp[idx] <= temp[idx + 1]:
            flag2 = True
            break
    return flag1 and flag2

idx = 1
bouncynum = 0
nonbouncy = 0
while True:
    if bouncy(idx):
        bouncynum += 1
    else:
        nonbouncy += 1
    if bouncynum / float(nonbouncy + bouncynum) == 0.99:
        break
    idx += 1



print bouncynum / float(nonbouncy + bouncynum)
print 'Bouncy is ' + str(bouncynum)
print 'Nonouncy is ' + str(nonbouncy)
print 'the sum is ' + str(nonbouncy + bouncynum)


