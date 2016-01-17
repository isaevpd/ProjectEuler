def is_palindrome_rec(s):
    if len(s) < 2:
        return True
    else:
        # print s
        s1 = s[-1]
        s2 = s[0]
        if s1 != s2:
            return False
        else:
            return is_palindrome_rec(s1[:-1]) and is_palindrome_rec(s2[1:])


print is_palindrome_rec('racecar')