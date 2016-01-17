import itertools

def pand(n):
    s = str(n)
    for letter in '123456789':
        if not letter in s:
            return False
    return True

def sub_string_div(n):
    str_of_n = str(n)
    values = {1:2,
              2:3,
              3:5,
              4:7,
              5:11,
              6:13,
              7:17}
    for idx in range(1, len(str_of_n) - 2):
        if int(str_of_n[idx:idx + 3]) % values[idx] != 0:
            return False
        
    return True



archive = set(itertools.permutations('1234567890'))
new = filter(lambda x: x[0] != '0', archive)
new_new = filter(lambda x: int(x), (''.join(tup) for tup in new))
new_new_new = filter(sub_string_div, (int(s) for s in new_new))





print sum(new_new_new)
