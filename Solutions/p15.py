def recursivePath(n, m):
    if n == 0 or m == 0:
        return 1
    return recursivePath(n - 1, m) + recursivePath(n, m - 1)

print recursivePath(2)