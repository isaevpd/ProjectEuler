def pal(n):
    return str(n) == str(n)[::-1]


def lynchrel(n):
    result = n
    for num in range(50):
        temp = result + int(str(result)[::-1])
        # print 'tmep is ', temp
        if pal(temp):
            return True
        result += int(str(result)[::-1])
    return False

# print lynchrel(4994)
result = 0

for num in range(10, 10000):
    if not lynchrel(num):
        result += 1

print result

