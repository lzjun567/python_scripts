"""
爬取微博评论，保存到文件中

https://m.weibo.cn/api/comments/show?id=4477013081328252&page=50
该接口能获取微博的前50页数据，每页10条， id 是某条微博的id


https://m.weibo.cn/comments/hotflow?mid=4477013081328252&max_id=330569188932643&max_id_type=0
此接口能爬到所有评论信息， mid 是某条微博id， max_id 是上一个请求返回的分页参数， max_id_type 固定为0就好
"""

from pymongo import MongoClient
import requests
import time

__author__ = 'liuzhijun'

headers = {
    "Host": "m.weibo.cn",
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) "
                  "Version/9.0 Mobile/13B143 Safari/601.1",
    "Cookie": "ALF=1585622740; SCF=AkYKPH_4_43DdgVfDGrD7N6PC2DQN3YlA5MS_Wtn7viiEfWYidSCeZUVClv83hcG0e3LaFPJMMOxfGELIzLciEY.; SUB=_2A25zX1GoDeRhGedI4lUW8CzOzz2IHXVQoH_grDV6PUJbktANLUzEkW1NVmpkfU6FYNoJwj2PzeF0Y9AMgJSdjT2J; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WWbbPzPaDijADNgfIppECPn5JpX5K-hUgL.Fo2c1KMNehzESh22dJLoIEXLxKMLBKnL12zLxK-LB.2L12qLxK-L1K2L1KnLxK-LB.qL1KMLxK-L1hqL1-zt; SUHB=0Ryr1hd10ceFZR; SSOLoginState=1583030776; _T_WM=68502013108; WEIBOCN_FROM=1110006030; MLOGIN=1; XSRF-TOKEN=6b73f7"
}

client = MongoClient('mongodb://localhost:27017/')
db = client['weibo']


def main(mid, max_id):
    """
    :param mid: 某条微博id
    :param max_id: 分页参数
    :return:
    """
    url = "https://m.weibo.cn/comments/hotflow?max_id_type=0"
    params = {"mid": mid}
    if max_id:
        params['max_id'] = max_id

    res = requests.get(url, params=params, headers=headers)
    print(res.content)
    result = res.json()
    max_id = result.get("data").get("max_id")
    data = result.get('data').get('data')
    for item in data:
        db['comment'].insert_one(item)

    if max_id:
        time.sleep(1)
        main(mid, max_id)


if __name__ == '__main__':
    main("4477013081328252", None)
