# encoding: utf-8

import json
import re
import time
from http.cookies import SimpleCookie

import jieba.analyse
import matplotlib.pyplot as plt
import requests
from scipy.misc import imread
from wordcloud import WordCloud

from pymongo import MongoClient


class Conn(object):
    client = MongoClient('localhost', 27017)
    db = client['weixin-comment']

    @classmethod
    def insert_many(cls, data):
        cls.db['comments'].insert_many(data)

    @classmethod
    def query(cls):
        data = cls.db['comments'].find()
        return data


conn = Conn()

raw_cookie = """
gsScrollPos-5517=; tvfe_boss_uuid=9c139f72f8ae693f; pac_uid=1_253421576; pgv_pvi=5182785536; RK=0IMfVbYuWK;
"""

cookie = SimpleCookie(raw_cookie)
requests_cookies = dict([(c, cookie[c].value) for c in cookie])


def main():
    # 普通留言, 精选留言总数
    normal_count, selected_count = 141, 100
    # 普通留言url
    normal_url = "https://mp.weixin.qq.com/misc/appmsgcomment?" \
                 "action=list_comment&" \
                 "mp_version=7&" \
                 "type=0&" \
                 "comment_id=2881104117&" \
                 "begin={begin}&" \
                 "count=10&" \
                 "token=1300595798&" \
                 "lang=zh_CN"

    # 精选留言url
    selected_url = "https://mp.weixin.qq.com/misc/appmsgcomment?action=list_comment&mp_version=7&type=1" \
                   "&begin={begin}&count=10&comment_id=2881104117&token=1300595798&lang=zh_CN"

    dd = dict([(normal_count, selected_url), (selected_count, normal_url)])

    for k, v in dd.items():
        crawler(k, v)


def crawler(count, url):
    for i in range(0, count, 10):
        r = requests.get(url.format(begin=i), cookies=requests_cookies)
        match = re.search(r'"comment":(\[\{.*\}\])', r.text, re.S)
        if match:
            data = json.loads(match.group(1), encoding="utf-8")
            conn.insert_many(data)
        time.sleep(1)


def display():
    # 读取数据

    data = conn.query()
    for c in data:
        yield c.get("content")


def word_segment(texts):
    # 分词处理
    jieba.analyse.set_stop_words("./stopwords.txt")
    for text in texts:
        tags = jieba.analyse.extract_tags(text, topK=20)
        yield " ".join(tags)


def generate_img(texts):
    # 生成词云图片
    data = " ".join(text for text in texts)

    mask_img = imread('./python-logo.png', flatten=True)
    wordcloud = WordCloud(
        font_path='/Library/Fonts//华文黑体.ttf',
        background_color='white',
        mask=mask_img
    ).generate(data)
    plt.imshow(wordcloud)
    plt.axis('off')
    plt.savefig('./wordcloud.jpg', dpi=600)


if __name__ == '__main__':
    main()
    # 生成词云方法
    # generate_img(word_segment(display()))
