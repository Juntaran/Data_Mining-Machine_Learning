# coding=utf-8

'''
    Author: Juntaran
    Email:  Jacinthmail@gmail.com
    Date:   2017/10/23 23:59
'''

from numpy import *

# 生成一个随机 4*4 数组
print random.rand(4, 4)

# 转化为矩阵 mat() 函数把数组转化为矩阵
randMat = mat(random.rand(4, 4))
print randMat

# 矩阵求逆
invRandMat = randMat.I
print invRandMat

# 矩阵相乘
print invRandMat * randMat