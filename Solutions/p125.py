import math

# runs in ~ 11 minutes

def is_palindrome(n):
    return str(n) == str(n)[::-1]

def last_is_first(n):
    last = n % 10
    while n >= 10:
        n /= 10
    return last == n 

def can_be_written(n):
    """
    returns True if a number can be written as 
    a sum of consequtive squares
    """
    max_number = round(math.sqrt(n))
    for num1 in xrange(int(max_number)):
        count = num1 + 1
        test = num1 * num1
        # multipliers = [num1, count]
        while test <= n:
            test += count * count
            count += 1
            # multipliers.append(count)
            if test == n:
                return True #, multipliers
    return False

# print can_be_written(595)


result = 0
# palindromes = []

for n in xrange(2, int(10**8)):
    print 10 ** 8 - n
    if n % 10 != 0 and last_is_first(n) and is_palindrome(n) and can_be_written(n):
        result += n
        # palindromes.append(n)

print result
# print palindromes


