def spiral_matrix(N):
    """
    returns N x N spiral matrix
    """
    matrix = [[0 for num1 in xrange(N)] for num2 in xrange(N)]

    count = N * N
    row = 0
    col = N - 1

    while count != 0:
        # print 'count is ' + str(count)
        while matrix[row][col] == 0:   # build top row from right to left
                matrix[row][col] = count
                col -= 1
                count -= 1

        col += 1 # get column back to where it was
        row += 1 # go down 1 row

        # for r in matrix:
        #     print r

        while row < N and matrix[row][col] == 0:   # build left column from top to bottom
            matrix[row][col] = count
            row += 1
            count -= 1

        row -= 1 # get row in the right position
        col += 1 # go right 1 column
        while col < N and matrix[row][col] == 0:
            matrix[row][col] = count
            col += 1
            count -= 1

        col -= 1 # get column in the right position  
        row -= 1 # go up 1 row

        while row > 0 and matrix[row][col] == 0:
            matrix[row][col] = count
            row -= 1
            count -= 1

        row += 1 # get row in the right position
        col -= 1 # get column in the right position

        # print row, col


    return matrix

# for row in spiral_matrix(100):
#     print row


def count_diagonal(M):
    result = 0
    row = 0
    col1 = 0
    col2 = len(M) - 1
    for dummy_idx in xrange(len(M)):
        result += M[row][col1]
        result += M[row][col2]
        row +=1
        col1 += 1
        col2 -= 1
    return result - 1

print count_diagonal(spiral_matrix(1001))



