import requests
from fake_useragent import UserAgent
import re

url = 'http://lol.qq.com/biz/hero/champion.js'
response = requests.get(url, headers={"User-Agent": UserAgent().random})
print(response.text)

result = re.findall(r'if(!LOLherojs)var LOLherojs={};LOLherojs.champion={"keys":(.+),"data"', response.text)
hero_str =re.findall(r'"keys":({.+?})', response.text)
hero_names = re.findall(r'"\d+":"(\w+)"',hero_str[0])
base_url ='http://lol.qq.com/biz/hero/{}.js'
for name in hero_names:
    hero_skins_respone = requests.get(base_url.format(name),headers={"User-Agent": UserAgent().random})
    img_ids = re.findall(r'id":"(\d+)"',re.findall(r'skins":.{(.+?)}.,',hero_skins_respone.text)[0])
    img_base_url ='http://ossweb-img.qq.com/images/lol/web201310/skin/big{}.jpg'
    for num in img_ids:
        response = requests.get(img_base_url.format(num),headers={"User-Agent": UserAgent().random})
        with open("img/"+name+num+'.jpg','wb') as f:
            f.write(response.content)