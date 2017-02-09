# coding=utf-8
import os
import re
import time

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


def parse_url_to_html(url, name):
    """
    解析URL，返回HTML内容
    :param url:解析的url
    :param name: 保存的html文件名
    :return: html
    """
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html5lib")
        # 正文
        body = soup.find_all(class_="x-wiki-content")[0]
        # 标题
        title = soup.find('h4').get_text()

        # 标题加入到正文的最前面，居中显示
        center_tag = soup.new_tag("center")
        title_tag = soup.new_tag('h1')
        title_tag.string = title
        center_tag.insert(1, title_tag)
        body.insert(1, center_tag)
        html = str(body)
        # body中的img标签的src相对路径的改成绝对路径
        pattern = "(<img .*?src=\")(.*?)(\")"

        def func(m):
            rtn = m.group(1) + "http://www.liaoxuefeng.com" + m.group(2) + m.group(3)
            return rtn

        html = re.compile(pattern).sub(func, html)
        html = html_template.format(content=html)
        with open(name, 'wb') as f:
            f.write(html)
        return name

    except Exception as e:
        print(e.message)


def get_url_list():
    """
    获取所有URL目录列表
    :return:
    """
    response = requests.get("http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000")
    soup = BeautifulSoup(response.content, "html5lib")
    menu_tag = soup.find_all(class_="uk-nav uk-nav-side")[1]
    urls = []
    for li in menu_tag.find_all("li"):
        url = "http://www.liaoxuefeng.com" + li.a.get('href')
        urls.append(url)
    return urls


def save_pdf(htmls, file_name):
    """
    把所有html文件保存到pdf文件
    :param htmls:  html文件列表
    :param file_name: pdf文件名
    :return:
    """
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
    pdfkit.from_file(htmls, file_name, options=options)


def main():
    start = time.time()
    urls = get_url_list()
    file_name = u"liaoxuefeng_Python3_tutorial.pdf"
    htmls = [parse_url_to_html(url, str(index) + ".html") for index, url in enumerate(urls)]
    save_pdf(htmls, file_name)

    for html in htmls:
        os.remove(html)

    total_time = time.time() - start
    print(u"总共耗时：%f 秒" % total_time)


if __name__ == '__main__':
    main()
