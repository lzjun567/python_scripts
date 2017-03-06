# encoding: utf-8
import csv

import requests

__author__ = 'liuzhijun'

# 头字段信息可以登录gold.xitu.io后查看

headers = {"X-LC-Id": "xxxx",
           "X-LC-Session": "xxxxxx",
           "X-LC-Sign": "xxx",
           "X-LC-UA": "xxxxx"}


def fetch_tags():
    # 获取所有标签
    url = "https://api.leancloud.cn/1.1/classes/Tag?where=%7B%7D&limit=1000"
    response = requests.get(url, headers=headers)
    print(response.content)

    with open('tags.csv', 'w') as csv_file:
        # colle:收藏,sub:关注,entries:文章,view:访问
        fieldnames = ['title', 'collectionsCount', 'subscribersCount', 'entriesCount', "viewsCount"]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for tag in response.json().get("results"):
            writer.writerow({'title': tag.get("title"),
                             'collectionsCount': tag.get("collectionsCount"),
                             "subscribersCount": tag.get("subscribersCount"),
                             "entriesCount": tag.get("entriesCount"),
                             "viewsCount": tag.get("viewsCount")})


def fetch_entites():
    # 获取所有文章
    max_page = 29820
    with open("entities.csv", 'w') as csv_file:
        for i in range(0, max_page, 20):
            url = "https://api.leancloud.cn/1.1/classes/Entry?where={}&limit=20&order=hotIndex&skip=%s"
            url = url % i
            response = requests.get(url, headers=headers)
            fieldnames = ("title", "viewsCount", "collectionCount", "commentsCount")
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            for tag in response.json().get("results"):
                writer.writerow({'title': tag.get("title"),
                                 'collectionCount': tag.get("collectionCount"),
                                 "commentsCount": tag.get("commentsCount"),
                                 "viewsCount": tag.get("viewsCount")})


if __name__ == '__main__':
    # fetch_tags()
    fetch_entites()
