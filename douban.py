#使用requests和xpath来爬取豆瓣电影相关信息，代码如下

import requests
from lxml import etree
import time

#豆瓣《神秘巨蛋》网址
url = "https://movie.douban.com/subject/26942674/?from=showing"

#requests.get()方法来获取页面的text
data = requests.get(url).text

#etree.HTML()来解析下载的页面数据“data”
s = etree.HTML(data)

#爬去电影名、编剧、主演、平分
file_name = s.xpath('//*[@id="content"]/h1/span[1]/text()')
directorName = s.xpath('//*[@id="info"]/span[2]/span[2]/a/text()')
#获取所有主演
actors = s.xpath('//*[@id="info"]/span[3]/span[2]/a/text()')
mark = s.xpath('//*[@id="interest_sectl"]/div[1]/div[2]/strong/text()')

#编剧可能多人，所以以列表的形式输出
dc = []
for i in directorName:
    dc.append(i)
 
#演员可能多人，所以以列表的形式输出   
ac = []
for i in actors:
    ac.append(i)
    
print("电影名：" , file_name)
print("编剧：" , dc)
print("演员：" , ac)
print("评分：",mark)
