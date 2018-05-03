# -*- coding: utf-8 -*-
# @Time    : 4/26/18 12:58 PM

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

red_heights = np.random.normal(50, 6, 10)
red_weights = np.random.normal(5, 0.5, 10)

blue_heights = np.random.normal(30, 6, 10)
blue_weights = np.random.normal(4, 0.5, 10)

red_linked = [i for i in map(lambda x, y: ((x, y), 'r'), red_heights, red_weights)]
blue_linked = [i for i in map(lambda x, y: ((x, y), 'b'), blue_heights, blue_weights)]

line_space_h = np.linspace(20, 60, 100)
line_space_w = np.linspace(2, 7, 100)

line_space_link = [line_space_w, line_space_h]

plt.scatter(red_weights, red_heights, c='r')
plt.scatter(blue_weights, blue_heights, c='b')


class KdTree():

    def __init__(self, point_list, depth=0, root=None):

        if len(point_list) > 0:

            # 选择的分类数
            k = len(point_list[0][0])

            # 切分轴的维度，根据分类数进行维度切换
            axis = depth % k

            # 按照相应维度排序数组
            point_list = sorted(point_list, key=lambda x: x[0][axis])

            # 中间值索引
            median = len(point_list) // 2

            # 特征点
            self.node = point_list[median]

            node_axis = self.node[0][axis]

            print('node_axis_here: {}'.format(node_axis))

            # 提取分割轴对应维度的坐标，并构造100个，方便下面绘图
            node_axis_squeeze = np.squeeze(np.asarray(np.full([1, 100], node_axis)))

            # 根据特征点的值绘图
            if axis == 0:
                plt.plot(line_space_link[0], node_axis_squeeze, c='g', linewidth=0.5)
            else:
                plt.plot(node_axis_squeeze, line_space_link[1], c='g', linewidth=0.5)

            # 树内元素个数
            self.size = len(point_list)
            self.root = root

            # 特征值，即分割线在相应维度的值
            self.node_value = point_list[median][0][axis]

            # 递归构造树节点
            if len(point_list[:median]) > 0:
                self.left = KdTree(point_list[:median], depth+1, self)
            else:
                self.left = None

            if len(point_list[median:]) > 0:
                self.right = KdTree(point_list[median + 1:], depth+1, self)
            else:
                self.right = None

            print('此时树的深度为{}'.format(depth))
            print('此时切分维度是{}'.format(axis))
            print('此时特征值索引为{}'.format(median))
            print('此时特征点为{}'.format(self.node))
            print('此时特征点对应分割轴的值为{}'.format(self.node_value))
            print('此时左树是{}'.format(self.left))
            print('此时右树是{}'.format(self.right))

        else:
            return

raw_data = list(np.concatenate((red_linked, blue_linked)))


print('raw_data here:{}'.format(raw_data))
tree = KdTree(raw_data)

plt.show()