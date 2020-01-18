import requests
from fake_useragent import UserAgent
from lxml import etree
import re
import pymongo
from time import sleep
import schedule

def get_data():
    url = 'https://www.jin10.com/'
    response = requests.get(url, headers={"User-Agent": UserAgent().random})
    response.encoding = 'utf-8'
    e = etree.HTML(response.text)

    all_time = [re.findall(r'news(\d+)', str)[0] for str in e.xpath('//div[@class="jin-flash_icon"]/a/@href')]
    simple_time = e.xpath('//div[@class="jin-flash_time"]/text()')
    contents = [str.xpath('string(.)') for str in e.xpath('//div[@class="jin-flash_b"]')]
    content_list = []
    for a_time, s_time, content in zip(all_time, simple_time, contents):
        content_list.append({"all_time": a_time, "simple_time": s_time, "content": content})
    return content_list


def get_collection():
    client = pymongo.MongoClient()
    collection = client.money.jin10
    return client, collection


def close_client(client):
    client.close()


def save_data(data, collection):
    data.reverse()
    for d in data:
        collection.insert(d)
        print(d)


def get_index(data_list, collection):
    index = 0
    for data in data_list:
        result = collection.find_one({'all_time': data['all_time']})
        if result:
            break
        else:
            index += 1
    return index

def main():
    data_list = get_data()
    index = get_index(data_list, collection)
    save_data(data_list[0:index], collection)

if __name__ == '__main__':
    client, collection = get_collection()
    schedule.every(10).seconds.do(main)
    while True:
        schedule.run_pending()
    close_client(client)
