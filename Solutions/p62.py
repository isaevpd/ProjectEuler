from itertools import permutations, combinations

# CUBES = set()

def is_perfect_cube(n):
    return round(n ** (1/3.)) ** 3 == n
    # return False

def get_root_number(n):
    # global CUBES
    digits = [int(x) for x in str(n)]
    n_digits = len(digits)
    n_power = n_digits - 1
    perms = permutations(digits)
    ans = filter(is_perfect_cube, set(sum(v * (10**(n_power - i)) for i, v in enumerate(item)) for item in perms))
    # ans = set(tup for tup in permutations(str(n), len(str(n))) if is_perfect_cube(int(''.join(tup))))
    # CUBES |= ans
    return len(ans)

def solve():
    n = 300
    while get_root_number(n ** 3) != 5:
        n += 1
        print n
        # print 'number of permutations of {} is:'.format(n), len(set(p for p in permutations(str(n ** 3), len(str(n ** 3)))))
        # break
    # print CUBES
    print 'Answer is', n
    print 'It"s permutations are ', set((filter(is_perfect_cube, [int(''.join(tup)) for tup in permutations(str(n ** 3), len(str(n ** 3))) if tup[0] != 0])))
    # print len(numbers)

solve()

# n = 41063625
# print get_root_number(41063625)



