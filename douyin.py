import re
from urllib.parse import urlparse

import requests

from . import utils

"""

作者：刘志军
公众号：Python之禅
任何问题可以加我微信：go2071  进行交流，备注“github”

"""


class DY(object):

    def __init__(self, app=None):
        self.app = app
        if app is not None:
            self.init_app(app)

        self.headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'zh-CN,zh;q=0.9',
            'cache-control': 'max-age=0',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1'
        }

        self.domain = ['www.douyin.com',
                       'v.douyin.com',
                       'www.snssdk.com',
                       'www.amemv.com',
                       'www.iesdouyin.com',
                       'aweme.snssdk.com']

    def init_app(self, app):
        self.app = app

    def parse(self, url):
        share_url = self.get_share_url(url)
        share_url_parse = urlparse(share_url)
        if share_url_parse.netloc not in self.domain:
            raise Exception("无效的链接")
        dytk = None
        vid = re.findall(r'\/share\/video\/(\d*)', share_url_parse.path)[0]
        match = re.search(r'\/share\/video\/(\d*)', share_url_parse.path)
        if match:
            vid = match.group(1)
        response = requests.get(share_url, headers=self.headers, allow_redirects=False)
        match = re.search('dytk: "(.*?)"', response.text)
        if match:
            dytk = match.group(1)

        if vid and dytk:
            return self.get_data(vid, dytk)
        else:
            raise Exception("解析失败")

    def get_share_url(self, url):
        response = requests.get(url,
                                headers=self.headers,
                                allow_redirects=False)
        if 'location' in response.headers.keys():
            return response.headers['location']
        else:
            raise Exception("解析失败")

    def get_data(self, vid, dytk):
        url = f"https://www.iesdouyin.com/web/api/v2/aweme/iteminfo/?item_ids={vid}&dytk={dytk}"
        response = requests.get(url, headers=self.headers, )
        result = response.json()
        if not response.status_code == 200:
            raise Exception("解析失败")
        item = result.get("item_list")[0]
        author = item.get("author").get("nickname")
        mp4 = item.get("video").get("play_addr").get("url_list")[0]
        cover = item.get("video").get("cover").get("url_list")[0]
        mp4 = mp4.replace("playwm", "play")
        res = requests.get(mp4, headers=self.headers, allow_redirects=True)
        mp4 = res.url
        desc = item.get("desc")
        mp3 = item.get("music").get("play_url").get("url_list")[0]

        data = dict()
        data['mp3'] = mp3
        data['mp4'] = mp4
        data['cover'] = cover
        data['nickname'] = author
        data['desc'] = desc
        data['duration'] = utils.format_duration(item.get("duration"))
        return data


dy = DY()

if __name__ == '__main__':
    dy = DY()
    data = dy.parse("https://v.douyin.com/oXbjfe/")
    import pprint
    pprint.pprint(data)

