#!/usr/bin/python3
'''
Python L2; Assignment #6
Write a code to overload __add__ method to perform  2 x 2 matrix addition
'''

class Matrix2x2(object):
    '''
    Matrix class for Assignment #6
    Add two or more matrix objects together
    '''

    def __init__(self, matrices):
        print("Matrix Class Constructor")
        self.matrices = matrices
        if len(matrices) > 2 or len(matrices) < 2:
            raise Exception("Only 2x2 Matrices Accepted")

    def __add__(self, o):
        result = [[0,0],[0,0]]
        if type(o) == type(self):
            for i in range(len(result)):
                for j in range(len(result)):
                    result[i][j] = o.matrices[i][j] + self.matrices[i][j]
        return result
    

matrices1 = [[3,4],[5,6]]
matrices2 = [[5,6],[7,8]]
mx1 = Matrix2x2(matrices1)
mx2 = Matrix2x2(matrices2)

print("{} + {} = {}".format(matrices1, matrices2, (mx1 + mx2)))


