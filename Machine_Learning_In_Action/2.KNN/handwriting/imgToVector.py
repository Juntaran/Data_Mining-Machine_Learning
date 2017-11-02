# coding=utf-8

'''
    Author: Juntaran
    Email:  Jacinthmail@gmail.com
    Date:   2017/11/2 19:51
'''

from numpy import *

def img2vector(filename):
    returnVect = zeros((1, 1024))
    fr = open(filename)
    for i in range(32):
        lineStr = fr.readline()
        for j in range(32):
            returnVect[0, 32*i+j] = int(lineStr[j])
    return returnVect

print img2vector('testDigits/0_13.txt')