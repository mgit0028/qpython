常见的彩票有双色球和大乐透，我们以这两种为例，用Python实现随机选号功能。

双色球

“双色球”每注投注号码由6个红色球号码和1个蓝色球号码组成。红色球号码从1–33中选择；蓝色球号码从1–16中选择。

import random

list_red = [x for x in range(1, 34)]      #1~33红色球序列
res = random.sample(list_red, 6)          #随机选取6个红球
res.sort()                                #对选取的6个红球排序
res.append(random.randint(1, 16))         #随机选取1个蓝球

print(res)


大乐透

“大乐透”的玩法是“35选5加12选2”，也就是前面35个数字选5个，后面12个数字选2个。

import random

list_red = [x for x in range(1,36)]        #1~35红色球序列
list_blue = [x for x in range(1,13)]       #1~12蓝色球序列

res_red = random.sample(list_red, 5)       #随机选取5个红球
res_blue = random.sample(list_blue, 2)     #随机选取2个红球

res_red.sort()                             #对选取的5个红球排序
res_blue.sort()                            #对选取的2个蓝球排序

res = res_red + res_blue
print(res)



很简单的算法，随机算法中我们用到的主要是random模块，关于random模块的更多用法可以参考我之前的博客：random模块

此外，还用到了python中的列表生成式，sort排序。
