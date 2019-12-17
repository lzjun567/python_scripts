"""
注意：代码基于Python3.6，不兼容python2
有疑问可通过公众号“Python之禅”联系作者
"""
import codecs
import csv
from urllib import parse

import requests
from pymongo import MongoClient

client = MongoClient()
db = client.xingqiu


def str_to_dict(s, join_symbol="\n", split_symbol=":"):
    """
    将字符串转换成dict对象
    :param s:
    :param join_symbol:
    :param split_symbol:
    :return:
    """
    s_list = s.split(join_symbol)
    data = dict()
    for item in s_list:
        item = item.strip()
        if item:
            k, v = item.split(split_symbol, 1)
            data[k] = v.strip()
    return data


# 直接从浏览器里面拷贝过来的，请替换成你自己的浏览器中的内容
headers = """
Accept: application/json, text.txt/plain, */*
Accept-Encoding: gzip, deflate, br
Accept-Language: zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7
Authorization: 8EAE71AC-081C-FE82-BE8C-954696
Connection: keep-alive
DNT: 1
Host: api.zsxq.com
Origin: https://wx.zsxq.com
Referer: https://wx.zsxq.com/dweb/
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36
X-Request-Id: 02001c28-fb3a-f027-20e7-8a1c458f3eee
X-Version: 1.10.0
"""

init_url = "https://api.zsxq.com/v1.10/groups/518855855524/topics?count=20"


def crawl(url):
    res = requests.get(url, headers=str_to_dict(headers))
    topics = res.json().get("resp_data").get("topics")
    if len(topics) <= 1:
        return
    for i in topics:
        print(i.get("talk").get("text.txt")[:10])
        db.topics.insert_one(i)
    else:
        last_time = i.get("create_time")
        crawl(url + "&end_time=" + parse.quote(last_time))


def statics():
    # 打卡
    talk = db.topics.aggregate(
        [
            {"$match": {"create_time": {"$gte": "2018-05-28T00:00:14.202+0800"}}},
            {
                "$group": {
                    "_id": {
                        "user_id": "$talk.owner.user_id",
                        "name": "$talk.owner.name",
                    },
                    "count": {"$sum": 1},
                }
            },
            {"$sort": {"count": -1}},
        ]
    )

    # 作业
    solution = db.topics.aggregate(
        [
            {"$match": {"create_time": {"$gte": "2018-05-28T00:00:14.202+0800"}}},
            {
                "$group": {
                    "_id": {
                        "user_id": "$solution.owner.user_id",
                        "name": "$solution.owner.name",
                    },
                    "count": {"$sum": 1},
                }
            },
            {"$sort": {"count": -1}},
        ]
    )

    data = dict()

    for item in talk:
        name = item.get("_id").get("name")
        if name:
            data[name] = {"talk": item.get("count")}

    for item in solution:
        name = item.get("_id").get("name")
        if name:
            data.setdefault(name, {}).update({"solution": item.get("count")})

    return data


if __name__ == "__main__":
    # 爬取数据并存储
    crawl(init_url)
    # 统计数据
    data = statics()
    # 统计写入cvs文件
    with codecs.open("names.csv", "w", "utf_8_sig") as csvfile:
        fieldnames = ["name", "talk", "solution"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for name, value in data.items():
            writer.writerow(
                {
                    "name": name,
                    "talk": value.get("talk"),
                    "solution": value.get("solution"),
                }
            )
