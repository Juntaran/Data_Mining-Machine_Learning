# coding=utf-8

'''
    Author: Juntaran
    Email:  Jacinthmail@gmail.com
    Date:   2017/11/6 15:39
'''

import decision_tree
import treePlotter

fr = open('lenses.txt')
lenses = [inst.strip().split('\t') for inst in fr.readlines()]
lensesLabels = ['age', 'prescript', 'astigmatic', 'tearRate']
lensesTrees = decision_tree.createTree(lenses, lensesLabels)
print lensesTrees

treePlotter.createPlot(lensesTrees)