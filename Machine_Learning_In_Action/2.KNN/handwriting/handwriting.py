# coding=utf-8

'''
    Author: Juntaran
    Email:  Jacinthmail@gmail.com
    Date:   2017/11/2 19:54
'''

from os import listdir
from imgToVector import *
from kNN import *

def handwritingClassTest():
    hwLabels = []

    # 获取目录内容
    trainingFileList = listdir('trainingDigits')
    m = len(trainingFileList)

    trainingMat = zeros((m, 1024))
    for i in range(m):
        # 从文件名解析分类数字
        fileNameStr = trainingFileList[i]
        fileStr = fileNameStr.split('.')[0]
        classNumStr = int(fileStr.split('_')[0])
        hwLabels.append(classNumStr)
        trainingMat[i, :] = img2vector('trainingDigits/%s' % fileNameStr)

    testFileList = listdir('testDigits')
    errorCount = 0.0
    mTest = len(testFileList)
    for i in range(mTest):
        fileNameStr = testFileList[i]
        fileStr = fileNameStr.split('.')[0]
        classNumStr = int(fileStr.split('_')[0])
        vectorUnderTest = img2vector('testDigits/%s' % fileNameStr)
        classifierResult = classify0(vectorUnderTest, trainingMat, hwLabels, 3)
        print "The classifier came back with: %d, the real answer is: %d" % (classifierResult, classNumStr)

        if classifierResult != classNumStr:
            errorCount += 1.0

    print "\nThe total number of errors is: %d" % errorCount
    print "\nThe total error rate is: %f" % (errorCount/float(mTest))

handwritingClassTest()