# # takes ~ 6 min to run with pypy

# def reversible(n):
#     reverse = str(n)[::-1]
#     if reverse[0] == '0':
#         return False
#     for digit in str(n + int(reverse)):
#         if int(digit) % 2 == 0:
#             return False
#     return True


# i = 0
# result = 0
# while i < 1e9:
#     # print i
#     if reversible(i):
#         result += 1
#     i += 1
# print result


li = 1000000000
res = 0
x = 10
while x < li:
    x += 1
    # if x % 1000000 == 0: print x / 1000000
    if x % 10 == 0: continue
    fl = False
    s = `x`
    """"""
    if s[0] in "02468" and s[-1] in "02468": continue 
    if s[0] in "13579" and s[-1] in "13579": continue
    """"""
    b = `x + int(s[::-1])`
    for s in b:
        if s in "02468":
            fl = True
            break
    if fl: continue
    #print x,b
    res += 1
print res