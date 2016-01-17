def is_abundant(n):
    return n < sum([idx for idx in xrange(1, n) if n % idx == 0]) #function to check if the number is abundant



abundant_numbers = [num for num in xrange(1, 28000) if is_abundant(num)]#generate abundant numbers

bad_numbers = set()

for num1 in abundant_numbers:
    for num2 in abundant_numbers:
        bad_numbers.add(num1 + num2) #loop to generate integers that CAN be expressed as a sum of 2 abundant numbers

print 'done with square loop' #make sure loop doesn't take too long

print sum(list(set(xrange(28000)) - set(bad_numbers))) #remove the numbers that can be expressed as 2 abundant numbers sum from regular integers

        

    
