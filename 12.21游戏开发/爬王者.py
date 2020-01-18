#爬取王者荣耀英雄图片
#导入所需模块

import requests
# request对象是从客户端向服务器发出请求，包括用户提交的信息以及客户端的一些信息。
# 客户端可通过HTML表单或在网页地址后面提供参数的方法提交数据，
# 然后服务器通过request对象的相关方法来获取这些数据
# request的各种方法主要用来处理客户端浏览器提交的请求中的各项参数和选项。
import os
# os模块提供了多数操作系统的功能接口函数。
# 当os模块被导入后，它会自适应于不同的操作系统平台，
# 根据不同的平台进行相应的操作，在python编程时，经常和文件、目录打交道，
# 所以离不了os模块。

#导入json文件（里面有所有英雄的名字及数字）

url='http://pvp.qq.com/web201605/js/herolist.json'  #英雄的名字json     真实地址
html = requests.get(url)

html_json=html.json()  #转化成json格式
#提取英雄名字和数字
hero_name=list(map(lambda x:x['cname'],html_json))  # 名字  Lambda 表达式  是一个匿名函数，即没有函数名的函数
hero_number=list(map(lambda x:x['ename'],html_json))  # 数字  遍历ename每个元素，执行lambda函数，并返回一个列表
def main():  #用于下载并保存图片
    ii=0
    # //game.gtimg.cn/images/yxzj/img201606/skin/hero-info/529/529-bigskin-2.jpg
    for v in hero_number:
        os.mkdir("D:\\111\\"+hero_name[ii])  # 创建文件夹
        os.chdir("D:\\111\\"+hero_name[ii])  # 进入刚刚创建的文件夹
        ii=ii+1
        for u in range(12):
            onehero_links='http://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/'+str(v)+'/'+str(v)+'-bigskin-'+str(u)+'.jpg'
            im = requests.get(onehero_links)#得到这个链接，请求这个链接
            if im.status_code == 200:  #返回的东西是否正常
               open(str(u), 'wb').write(im.content)

main()