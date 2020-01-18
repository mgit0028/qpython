#!/usr/bin/python
# -*- coding: UTF-8 -*-

import random

list_red = [x for x in range(1, 34)]      #1~33红色球序列
res = random.sample(list_red, 6)          #随机选取6个红球
res.sort()                                #对选取的6个红球排序
res.append(random.randint(1, 16))         #随机选取1个蓝球

print(res)
