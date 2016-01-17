from datetime import date, timedelta

d0 = date(1901, 1, 1)
d1 = date(2000, 12, 31)

result = 0
while d0 != d1:
    print d0
    if d0.day == 1 and d0.weekday() == 6:
        result += 1
    d0 += timedelta(days=1)

print result

# # for idx in xrange(5):
# #     print d0 + timedelta(idx)
# # print timedelta(days=1)
# d0 += timedelta(days=32)

# print d0
