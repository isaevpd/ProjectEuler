def pand(s):
    if '0' in s:
        return False
    if len(set(s)) != 9:
        return False
    return True
    # return set(s) == set('123456789')

# print pand('123456789'[-7:])


# s = '192748023123456798'
# print pand(s[-9:])

# print ('12341235567899459384759123'[-9:])
k = 0
a = 1
b = 1

while True:
    k += 1
    print k
    if a % 10 != 0:
        if pand(str(a)[0:9]) and pand(str(a)[-9:]):         
            # print a
            print k
            break
    a, b = b, a + b