for num1 in range(5):
    print 'num1 is ' + str(num1)
    for num2 in range(5):
        print 'num2 is ' + str(num2)
        print 'num1 is ' + str(num1)
        print num1 == num2
        if num1 != num2:
            print 'breaking'
            break
        for num3 in range(5):
                print 'num 3 is ' + str(num3)