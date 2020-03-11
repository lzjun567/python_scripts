# coding=utf-8
from __future__ import unicode_literals

import logging
import os
import re
import time

try:
    from urllib.parse import urlparse  # py3
except:
    from urlparse import urlparse  # py2

import pdfkit
import requests
from bs4 import BeautifulSoup

html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
</head>
<body>
{content}
</body>
</html>

"""
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36",
    "Host": "mp.weixin.qq.com",
    "Cookie": "ua_id=drrGOcRzPtgj6vQxAAAAAPRcWHFwYqh865SBhBSf_Uc=; mm_lang=zh_CN; pgv_pvi=4252107776; noticeLoginFlag=1; pgv_pvid=3153415252; RK=uJJdBbYcWq; ptcz=597ba21975613de87ee9592ae38a116dbcc42c2a0cf8e47f1cfc430801f56001; ts_uid=6305021634; tvfe_boss_uuid=783a31d70f081c78; mobileUV=1_16993e5d8b7_9f488; ptui_loginuin=253421576; openid2ticket_ow-uujmHSiUtZWYpm7jDnwkAnt44=U+VV2NT+PyTCFbzEW4rmUDgsXydE5yDeO1GsTAJJZCA=; openid2ticket_oPGiXjhP6KzS5g8fMV3OHuuZkwmg=f2yHQT8ds8O8g46OyohfPyVCBbSvnnFtgwCf/aGHAYk=; o_cookie=253421576; pac_uid=1_253421576; xid=d7f448a2b6831b0f672adc526643b20a; rewardsn=; wxtokenkey=777",
}


class Crawler(object):
    """
    爬虫基类，所有爬虫都应该继承此类
    """
    name = None

    def __init__(self, name, start_url):
        """
        初始化
        :param name: 将要被保存为PDF的文件名称
        :param start_url: 爬虫入口URL
        """
        self.name = name
        self.start_url = start_url
        self.domain = '{uri.scheme}://{uri.netloc}'.format(uri=urlparse(self.start_url))

    @staticmethod
    def request(url, **kwargs):
        """
        网络请求,返回response对象
        :return:
        """
        response = requests.get(url, **kwargs)
        return response

    def parse_menu(self, response):
        """
        从response中解析出所有目录的URL链接
        """
        raise NotImplementedError

    def parse_body(self, response):
        """
        解析正文,由子类实现
        :param response: 爬虫返回的response对象
        :return: 返回经过处理的html正文文本
        """
        raise NotImplementedError

    def run(self):
        start = time.time()
        options = {
            'page-size': 'Letter',
            'margin-top': '0.75in',
            'margin-right': '0.75in',
            'margin-bottom': '0.75in',
            'margin-left': '0.75in',
            'encoding': "UTF-8",
            'custom-header': [
                ('Accept-Encoding', 'gzip')
            ],
            'cookie': [
                ('cookie-name1', 'cookie-value1'),
                ('cookie-name2', 'cookie-value2'),
            ],
            'outline-depth': 10,
        }
        htmls = []
        for index, url in enumerate(self.parse_menu(None)):
            html = self.parse_body(self.request(url,  headers=headers))
            f_name = ".".join([str(index), "html"])
            with open(f_name, 'wb') as f:
                f.write(html)
            htmls.append(f_name)

        pdfkit.from_file(htmls, self.name + ".pdf", options=options)
        for html in htmls:
            os.remove(html)
        total_time = time.time() - start
        print(u"总共耗时：%f 秒" % total_time)


class LiaoxuefengPythonCrawler(Crawler):
    """
    廖雪峰Python3教程
    """

    def parse_menu(self, response):
        """
        解析目录结构,获取所有URL目录列表
        :param response 爬虫返回的response对象
        :return: url生成器
        """
        htmls = [
            "http://mp.weixin.qq.com/s?__biz=MjM5MzgyODQxMQ==&mid=2650371855&idx=1&sn=2f15cdfe0b5896b2df7705154571c1b5&chksm=be9ccc5b89eb454d18bb646f3e348a100fe2af38327c947999d047d66d1663f7892afe0044b9&scene=27#wechat_redirect",
            "http://mp.weixin.qq.com/s?__biz=MjM5MzgyODQxMQ==&mid=2650371847&idx=1&sn=5cfac634f11913f99c2d1587d0433a53&chksm=be9ccc5389eb45453e0576ee0d949472f61fbe9daea46183494ad1b8f91a367bc36adcf017f2&scene=27#wechat_redirect",
            "http://mp.weixin.qq.com/s?__biz=MjM5MzgyODQxMQ==&mid=2650371826&idx=1&sn=7a76628812a3949b0ec1a308ceec3051&chksm=be9ccda689eb44b0f3b0f8327fd4626ea3f1b888b4e755c4c5a2dbeb88954138b73b61887177#rd",
            "http://mp.weixin.qq.com/s?__biz=MjM5MzgyODQxMQ==&mid=2650371809&idx=1&sn=c7be295675b11f94b6b33b8c996e9aa9&chksm=be9ccdb589eb44a3cd215766ba3460415e54b9cfa763409689eea789cd47195e1b689f3a09ca&scene=27#wechat_redirect",
            "http://mp.weixin.qq.com/s?__biz=MjM5MzgyODQxMQ==&mid=2650371794&idx=1&sn=5afc8a0e65cbe939467ce87a1c68f547&chksm=be9ccd8689eb4490986dc5be626c8c755406926262da94b7014d8aad29d631cd62ec14a907a4&scene=27#wechat_redirect",
            "http://mp.weixin.qq.com/s?__biz=MjM5MzgyODQxMQ==&mid=2650371769&idx=1&sn=2f20c33c2454c5ec68792c081d5998f1&chksm=be9ccded89eb44fbda608edc9103d4d62430bb0adf182383e8c20474aa354faad07b24952db2#rd",
            "http://mp.weixin.qq.com/s?__biz=MjM5MzgyODQxMQ==&mid=2650371760&idx=1&sn=0ebd9f172de570ec3b10ab0ed5aa9c63&chksm=be9ccde489eb44f2549fcf9ae0c555109d952dc6db8e8e7c4024ae64372016c9cc78e63f13ac&scene=27#wechat_redirect",
            "http://mp.weixin.qq.com/s?__biz=MjM5MzgyODQxMQ==&mid=2650371704&idx=1&sn=0145ca19dabc03cda6ac860caf0c2dd0&chksm=be9ccd2c89eb443ab809e05484f58da87aa1ba2b0e678fbd2a06b0ba2c4df600d001e86d6838&scene=27#wechat_redirect",
            "http://mp.weixin.qq.com/s?__biz=MjM5MzgyODQxMQ==&mid=2650371678&idx=1&sn=de791b0341e9075064b02124af1fe864&chksm=be9ccd0a89eb441c54837140cfa0c3070431dc2c4fa0fb8a64a91419dd7923490273dff305c8&scene=27#wechat_redirect",
            "http://mp.weixin.qq.com/s?__biz=MjM5MzgyODQxMQ==&mid=2650371650&idx=1&sn=48fd3821d43dd7374813618be0b3d42c&chksm=be9ccd1689eb4400fa0b42e9ec6676607caf93916071ca909715d05e2d4246af5cf81a8c17f3&scene=27#wechat_redirect"
        ]
        return htmls

    def parse_body(self, response):
        """
        解析正文
        :param response: 爬虫返回的response对象
        :return: 返回处理后的html文本
        """
        try:
            return response.content
            # soup = BeautifulSoup(response.content, 'html.parser')
            # body = soup
            #
            # # 加入标题, 居中显示
            # title = soup.find('h4').get_text()
            # center_tag = soup.new_tag("center")
            # title_tag = soup.new_tag('h1')
            # title_tag.string = title
            # center_tag.insert(1, title_tag)
            # body.insert(1, center_tag)
            #
            # html = str(body)
            # html = html.encode("utf-8")
            # return html
        except Exception as e:
            logging.error("解析错误", exc_info=True)


if __name__ == '__main__':
    start_url = "http://www.liaoxuefeng.com/wiki/0013739516305929606dd18361248578c67b8067c8c017b000"
    crawler = LiaoxuefengPythonCrawler("廖雪峰Git", start_url)
    crawler.run()
