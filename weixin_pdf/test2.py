import os
import time

import pdfkit
import requests

options = {
    'page-size': 'Letter',
    'margin-top': '0.75in',
    'margin-right': '0.75in',
    'margin-bottom': '0.75in',
    'margin-left': '0.75in',
    'encoding': "UTF-8",
    'outline-depth': 10,
}


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

    def __init__(self, name):
        """
        初始化
        :param name: 将要被保存为PDF的文件名称
        :param start_url: 爬虫入口URL
        """
        self.name = name

    @staticmethod
    def request(url, **kwargs):
        """
        网络请求,返回response对象
        :return:
        """
        response = requests.get(url, **kwargs)
        return response


    def parse_body(self, response):
        """
        解析正文
        :param response: 爬虫返回的response对象
        :return: 返回处理后的html文本
        """
        content = response.text.replace("data-src", 'src')
        return content

    def run(self, urls):
        start = time.time()
        htmls = []
        for index, url in enumerate(urls):
            f_name = ".".join([str(index), "html"])
            if not os.path.exists(f_name):
                # 方便失败后重试
                html = self.parse_body(self.request(url, headers=headers))
                with open(f_name, 'w', encoding="utf-8") as f:
                    f.write(html)
            htmls.append(f_name)

        pdfkit.from_file(htmls, self.name + ".pdf", options=options)
        for html in htmls:
            os.remove(html)
        total_time = time.time() - start
        print(u"总共耗时：%f 秒" % total_time)


if __name__ == '__main__':
    crawler = Crawler("歪理邪说")

    with open("url.txt") as f:
        urls = f.readlines()

    crawler.run(urls)
