# coding=utf-8

'''
    Author: Juntaran
    Email:  Jacinthmail@gmail.com
    Date:   2017/10/24 00:56
'''

import matplotlib.pyplot as plt
from kNN import *

fig = plt.figure()
# 将画布分割成 1 行 1 列，图像画在从左到右从上到下的第 1 块
ax = fig.add_subplot(111)

datingDataMat, datingLabels = file2matrix('datingTestSet2.txt')
normMat, ranges, minVals = autoNorm(datingDataMat)

# ax.scatter(datingDataMat[:, 1], datingDataMat[:, 2])
ax.scatter(datingDataMat[:, 0], datingDataMat[:, 1], 15.0*array(datingLabels), 15.0*array(datingLabels))
plt.show()