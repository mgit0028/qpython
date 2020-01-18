import requests
from fake_useragent import UserAgent
from lxml import etree

url = 'http://www.farmer.com.cn/xwpd/rdjj1/201807/t20180731_1394806.htm'

response = requests.get(url, headers={"User-Agent": UserAgent().random})
print(response.text)

e = etree.HTML(response.text)

title = e.xpath('//h1/text()')
content = e.xpath('string(//div[@class="TRS_Editor"])')
imgs = e.xpath('//div[@class="TRS_Editor"]//img/@src')
