# encoding: utf-8
# !/usr/bin/env python

import requests

from bs4 import BeautifulSoup

headers = headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.86 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate",
    "Host": "www.zhihu.com",
    "Upgrade-Insecure-Requests": "1",
}
response = requests.get("https://www.zhihu.com", headers=headers)
soup = BeautifulSoup(response.content, "html.parser")
xsrf = soup.find('input', attrs={"name": "_xsrf"}).get("value")
print(xsrf)
# print(response.content)

data = {
    "_xsrf": xsrf,
    "password": "xxx",
    "captcha": "pvRJ",
    "email": "xxxxxx",
}
# _xsrf=ef85127d992f6ea39d9817bbb7a315d4&password=lzjun854979&captcha=ENTV&email=lzjun567%40qq.com
with open("text.gif", "wb") as f:
    f.write(requests.get("https://www.zhihu.com/captcha.gif?r=1490697036809&type=login", headers=headers).content)

captcha = input()

data['captcha'] = captcha

print(data)
import json
response = requests.post("https://www.zhihu.com/login/email", headers=headers, data=json.dumps(data))
print(response.content)
print(response.json().get("data").get("captcha"))
print(response.json().get("data").get("account"))
import re

s = "sdfdf 12:22:23 dsfsdf 23:23:12"
print(re.compile(r"(\d{2}:\d{2}:\d{2})").findall(s))
