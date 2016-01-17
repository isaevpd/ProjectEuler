def helper(n):
    """
    input: integer n
    output: tuple of multipliers 
    that result in a pandigital 
    number 1-9
    e.g. helper(192) == (1, 2, 3)
    """
    result = ()
    s = list('123456789')
    temp = ''
    i = 1
    while sorted(temp) != s:
        # print sorted(temp)
        temp += str(n * i)
        result += (i, )
        if len(temp) > len(s):
            return False
        i += 1
    return temp


results = dict()
for num in range(100000):
    if helper(num):
        results[helper(num)] = num

print max(results)