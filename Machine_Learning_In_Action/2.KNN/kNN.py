# coding=utf-8

'''
    Author: Juntaran
    Email:  Jacinthmail@gmail.com
    Date:   2017/10/24 00:26
'''

from numpy import *
import operator

def createDataSet():
    group = array( [1.0, 1.1],
                   [1.0, 1.0],
                   [0, 0],
                   [0, 0,1])
    labels = ['A', 'A', 'B', 'B']
    return group, labels

# inX: 用于分类的输入向量
# labels: 数量与矩阵 dataSet 的行数相同
def classify0(inX, dataSet, labels, k):

    dataSetSize = dataSet.shape[0]

    # 距离计算
    diffMat = tile(inX, (dataSetSize, 1)) - dataSet
    sqDiffMat = diffMat ** 2
    sqDistances = sqDiffMat.sum(axis=1)
    distances = sqDistances ** 0.5

    sortedDistIndicies = distances.argsort()
    classCount = {}

    # 选择距离最小的 k 个点
    for i in range(k):
        voteLabel = labels[sortedDistIndicies[i]]
        classCount[voteLabel] = classCount.get(voteLabel, 0) + 1

    # 排序
    sortedClassCount = sorted(classCount.iteritems(), key=operator.itemgetter(1), reverse=True)

    return sortedClassCount[0][0]

# 文件转化为矩阵
def file2matrix(filename):

    # 获取文件行数
    fr = open(filename)
    arrayOLines = fr.readlines()
    numberOfLines = len(arrayOLines)

    # 创建返回的 NumPy 矩阵
    returnMat = zeros((numberOfLines, 3))
    classLabelVector = []
    index = 0

    # 解析文件数据到列表
    for line in arrayOLines:
        line = line.strip()
        listFromLine = line.split('\t')

        # 选取前三个元素存储到特征矩阵
        returnMat[index, :] = listFromLine[0:3]
        classLabelVector.append(int(listFromLine[-1]))
        index += 1

    return returnMat, classLabelVector

# 归一化特征值
def autoNorm(dataSet):
    minVals = dataSet.min(0)
    maxVals = dataSet.max(0)
    ranges = maxVals - minVals
    normDataSet = zeros(shape(dataSet))
    m = dataSet.shape[0]
    normDataSet = dataSet - tile(minVals, (m,1))
    # 特征值相除
    normDataSet = normDataSet/tile(ranges, (m,1))
    return normDataSet, ranges, minVals




datingDataMat, datingLabels = file2matrix('datingTestSet2.txt')
print datingDataMat
print datingLabels
print datingLabels[0:20]

normMat, ranges, minVals = autoNorm(datingDataMat)
print normMat
print ranges
print minVals