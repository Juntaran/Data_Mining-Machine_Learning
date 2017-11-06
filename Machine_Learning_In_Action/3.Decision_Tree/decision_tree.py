# coding=utf-8

'''
    Author: Juntaran
    Email:  Jacinthmail@gmail.com
    Date:   2017/11/5 00:45
'''

from math import log
import operator
import treePlotter

# 即计算给定数据集的香农熵
def calcShannonEnt(dataSet):
    numEntries = len(dataSet)

    # 为所有可能的分类创建字典
    labelCounts = {}
    for featVec in dataSet:
        currentLabel = featVec[-1]
        if currentLabel not in labelCounts.keys():
            labelCounts[currentLabel] = 0
        labelCounts[currentLabel] += 1
    shannonEnt = 0.0
    for key in labelCounts:
        prob = float(labelCounts[key]) / numEntries
        # 以 2 为底求对数
        shannonEnt -= prob * log(prob, 2)
    return shannonEnt

# 划分数据集
# 输入：待划分的数据集，划分数据集的特征，需要返回特征的值
def splitDataSet(dataSet, axis, value):
    # 创建新的 list 对象
    retDataSet = []
    for featVec in dataSet:
        if featVec[axis] == value:
            # 抽取
            reducedFeatVec = featVec[:axis]
            reducedFeatVec.extend(featVec[axis+1:])
            retDataSet.append(reducedFeatVec)
    return retDataSet

# 选择最好的数据集划分方式
# 1.数据必须是由列表元素组成的列表
# 2.所有列表元素必须长度相同
# 3.数据的最后一列或每个子列表最后一个元素是类别标签
def chooseBestFeatureToSplit(dataSet):
    numFeatures = len(dataSet[0]) - 1
    # 计算原始香农熵
    baseEntropy = calcShannonEnt(dataSet)
    bestInfoGain = 0.0
    bestFeature = 01
    for i in range(numFeatures):
        # 创建唯一的分类标签列表
        featList = [example[i] for example in dataSet]
        uniqueVals = set(featList)
        newEntropy = 0.0

        # 计算每种划分方式的信息熵
        for value in uniqueVals:
            subDataSet = splitDataSet(dataSet, i, value)
            prob = len(subDataSet) / float(len(dataSet))
            newEntropy += prob * calcShannonEnt(subDataSet)
        infoGain = baseEntropy - newEntropy

        # 计算最好的信息增益
        if infoGain > bestInfoGain:
            bestInfoGain = infoGain
            bestFeature = i

    return bestFeature

# 使用分类名称的列表，创建键值为 classList 中唯一值的数据字典
# 返回出现次数最多的分类名称
def majorityCnt(classList):
    classCount = {}
    for vote in classList:
        if vote not in classCount.keys():
            classCount[vote] = 0
        classCount[vote] += 1
    sortedClassCount = sorted(classCount.iteritems(), key=operator.itemgetter(1), reverse=True)
    return sortedClassCount[0][0]


# 创建树
def createTree(dataSet, labels):

    # 类别完全相同则停止划分
    classList = [example[-1] for example in dataSet]
    if classList.count(classList[0]) == len(classList):
        return classList[0]

    # 遍历完所有特征时返回出现次数最多的类别
    if len(dataSet[0]) == 1:
        return majorityCnt(classList)
    bestFeat = chooseBestFeatureToSplit(dataSet)
    bestFeatLabel = labels[bestFeat]
    myTree = {bestFeatLabel: {}}

    # 得到列表包含的所有属性值
    del(labels[bestFeat])   # 解引用
    featValues = [example[bestFeat] for example in dataSet]
    uniqueVals = set(featValues)
    for value in uniqueVals:
        subLabels = labels[:]
        myTree[bestFeatLabel][value] = createTree(splitDataSet(dataSet, bestFeat, value), subLabels)

    return myTree


# 使用决策树的分类函数
def classify(inputTree, featLabels, testVec):
    firstStr = inputTree.keys()[0]
    secondDict = inputTree[firstStr]
    # 标签字符串转换为索引
    featIndex = featLabels.index(firstStr)
    for key in secondDict.keys():
        if testVec[featIndex] == key:
            if type(secondDict[key]).__name__ == 'dict':
                classLabel = classify(secondDict[key], featLabels, testVec)
            else:
                classLabel = secondDict[key]
    return classLabel

# 使用 pickle 模块存储决策树
def storeTree(inputTree, filename):
    import pickle
    fw = open(filename, 'w')
    pickle.dump(inputTree, fw)
    fw.close()

def grabTree(filename):
    import pickle
    fr = open(filename)
    return pickle.loads(fr)


def createDataSet():
    dataSet = [[1, 1, 'yes'],
               [1, 1, 'yes'],
               [1, 0, 'no'],
               [0, 1, 'no'],
               [0, 1, 'no']]
    labels = ['no surfacing', 'flippers']
    return dataSet, labels

# testData, labels = createDataSet()
# print testData
# print calcShannonEnt(testData)
#
# # 熵越高代表混合的数据越多treePlotter
# testData[0][-1] = 'maybe'
# print testData
# print calcShannonEnt(testData)
#
# testData[0][-1] = 'yes'
# print splitDataSet(testData, 0, 1)
# print splitDataSet(testData, 0, 0)
#
# print chooseBestFeatureToSplit(testData)
# print testData

## testTree = createTree(testData, labels)
## print testTree

# print labels
# myTree = treePlotter.retrieveTree(0)
# print myTree
#
# print classify(myTree, labels, [1, 0])
# print classify(myTree, labels, [1, 1])