#!/usr/bin/python3

#
# Exercise - 1
# Filename: ex1.py
#

#
# Implement the function ruler() which takes a number (for example, 43) as argument,
# and produces output as shown below.
#
#           1         2         3         4
#  1234567890123456789012345678901234567890123
#
#  (note: 1st row values are aligned to respective 0s of the 2nd row)
##################################################################################
def ruler(n):
    if n > 0:
        r1 = int(n/10)
        r2 = n

        # Row 1...
        for i in range(1, (r1+1)):
            print("         " + str(i), end='')
        print()

        # Row 2...
        for i in range(1, (r1+1)):
            for j in range(1,10):
                print(str(j), end='')
            print("0", end='')

        # print remainder...
        for i in range(1, ((r2%10)+1)):
            print(str(i), end='')
        print()

    else:
        return

    return


#  Test correctness of the function with the following values : 5, 10, 25, 51 and 80
ruler(5)
ruler(10)
ruler(25)
ruler(51)
ruler(80)

