# encoding: utf-8
# !/usr/bin/env python

import time
from pymongo import MongoClient
import requests
from datetime import timedelta
import re
from bs4 import BeautifulSoup
from tornado import httpclient, gen, ioloop, queues

__author__ = 'liuzhijun'

concurrency = 10

headers = {
    'Connection': 'Keep-Alive',
    'Accept': 'text/html, application/xhtml+xml, */*',
    'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Sa",
    "Referer": "http://www.jobbole.com/",
}


@gen.coroutine
def get_posts_url_from_page(page_url):
    """
    获取指定页面中所有文章的URL
    :param page_url
    :return:
    """
    try:
        response = yield httpclient.AsyncHTTPClient().fetch(page_url, headers=headers)
        soup = BeautifulSoup(response.body, 'html.parser')
        posts_tag = soup.find_all('div', class_="post floated-thumb")
        urls = []
        for index, archive in enumerate(posts_tag):
            meta = archive.find("div", class_="post-meta")
            url = meta.p.a['href']
            urls.append(url)
        raise gen.Return(urls)
    except httpclient.HTTPError as e:
        print('Exception: %s %s' % (e, page_url))
        raise gen.Return([])


@gen.coroutine
def get_post_data_from_url(post_url, cookies):
    """
    获取文章的元信息:阅读数\点赞数\收藏数\评论
    :param post_url:
    :return:
    """
    try:
        headers["Cookie"] = ";".join([name + "=" + value for name, value in cookies.items()])
        response = yield httpclient.AsyncHTTPClient().fetch(post_url, headers=headers)
        soup = BeautifulSoup(response.body, 'html.parser')
        title = soup.find("div", class_="entry-header").get_text()
        meta_tag = soup.find("div", class_="entry-meta").p
        text = meta_tag.get_text()

        def extract_keyword(pattern, content):
            """
            利用正则表达式提取匹配的内容
            """
            match = re.compile(pattern, flags=re.S).search(content)
            if match:
                return int(match.group(1).replace(",", '').replace(" ", "0"))
            else:
                return 0

        read_count = extract_keyword("([\d,]+) 阅读", text)
        comment_count = extract_keyword("([\d,]+) 评论", text)

        post_adds = soup.find("div", class_="post-adds")

        vote_count = extract_keyword("([\d, ]+) 赞", post_adds.find("span", class_="vote-post-up").get_text())
        bookmark_count = extract_keyword("([\d, ]+) 收藏", post_adds.find("span", class_="bookmark-btn").get_text())

        post_data = {"url": post_url,
                     "title": title,
                     "read_count": read_count,
                     "comment_count": comment_count,
                     "vote_count": vote_count,
                     "bookmark_count": bookmark_count}
        print(title)
        raise gen.Return(post_data)
    except httpclient.HTTPError as e:
        print('Exception: %s %s' % (e, post_url))
        raise gen.Return({})



@gen.coroutine
def mainx():
    start = time.time()
    fetched = 0
    client = MongoClient('mongodb://localhost:27017/')
    db = client['posts']
    cookies = {
        'wordpress_logged_in_0efdf49af511fd88681529ef8c2e5fbf': 'liuzhijun%7C1489462391%7CcFSvpRWbyJcPRGSIelRPWRIqUNdIQnF5Jjh1BrBPQI2%7C812c5106ea45baeae74102845a2c6d269de6b7547e85a5613b575aa9c8708add',
        'wordpress_0efdf49af511fd88681529ef8c2e5fbf': 'liuzhijun%7C1489462391%7CcFSvpRWbyJcPRGSIelRPWRIqUNdIQnF5Jjh1BrBPQI2%7C0edb104a0e34927a3c18e3fc4f10cc051153b1252f1f74efd7b57d21613e1f92'}
    post_queue = queues.Queue()
    page_queue = queues.Queue()
    for i in range(1, 69):
        page_url = "http://python.jobbole.com/all-posts/page/{page}/".format(page=i)
        page_queue.put(page_url)
        print(page_url)

    @gen.coroutine
    def posts_url_worker():
        while True:
            page = yield page_queue.get()
            urls = yield get_posts_url_from_page(page)
            for u in urls:
                post_queue.put(u)
            page_queue.task_done()

    @gen.coroutine
    def post_data_worker():
        while True:
            url = yield post_queue.get()
            post = yield get_post_data_from_url(url, cookies)
            nonlocal fetched
            fetched += 1
            db.posts.insert_one(post)
            post_queue.task_done()

    for _ in range(concurrency):
        posts_url_worker()
    for _ in range(concurrency):
        post_data_worker()

    yield page_queue.join()
    yield post_queue.join()
    # yield q.join(timeout=timedelta(seconds=300))
    print('爬取%s 篇文章,总共耗时%d 秒.' % (fetched, time.time() - start))


def login():
    """
    登录账户,获取登录cookie信息
    :return:
    """
    url = "http://python.jobbole.com/wp-admin/admin-ajax.php"
    account = {"action": "user_login",
               "user_login": "liuzhijun",
               "user_pass": "**********",
               "remember_me": "1"}
    response = requests.post(url, data=account)
    print(response.cookies)
    cookies = dict((name, value) for name, value in response.cookies.items())
    return cookies


if __name__ == '__main__':
    # print(login())
    #
    # import logging
    #
    # logging.basicConfig()
    io_loop = ioloop.IOLoop.current()
    # io_loop.run_sync(main)
    # io_loop.run_sync(lambda: get_all_post_url(67))
    cookies = {
        'wordpress_logged_in_0efdf49af511fd88681529ef8c2e5fbf': 'liuzhijun%7C1489462391%7CcFSvpRWbyJcPRGSIelRPWRIqUNdIQnF5Jjh1BrBPQI2%7C812c5106ea45baeae74102845a2c6d269de6b7547e85a5613b575aa9c8708add',
        'wordpress_0efdf49af511fd88681529ef8c2e5fbf': 'liuzhijun%7C1489462391%7CcFSvpRWbyJcPRGSIelRPWRIqUNdIQnF5Jjh1BrBPQI2%7C0edb104a0e34927a3c18e3fc4f10cc051153b1252f1f74efd7b57d21613e1f92'}

    # io_loop.run_sync(lambda: get_post_data_from_url("http://python.jobbole.com/87288/", cookies))
    io_loop.run_sync(mainx)
