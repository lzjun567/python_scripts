# encoding: utf-8
from tornado import httpclient, gen, ioloop, queues
from pymongo import MongoClient
import time
import json
import datetime
import re

__author__ = 'liuzhijun'

client = MongoClient('mongodb://localhost:27017/')
db = client['juejin']

concurrency = 10

headers = {
    'Connection': 'Keep-Alive',
    'Accept': 'text/html, application/xhtml+xml, */*',
    'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36",
    "HOST": "api.leancloud.cn",
    "X-LC-Id": "mhke0kuv33myn4t4ghuid4oq2hjj12li374hvcif202y5bm6",
    "X-LC-Session": "umqpblpaq3z3keam1mk1ktqay",
    "X-LC-Sign": "1ac2e8eb9c6c71fcbc746f277638bc0d,1487824152948",
    "X-LC-UA": "AV/js1.5.0",
}


@gen.coroutine
def parse(url):
    try:
        print(url)
        response = yield httpclient.AsyncHTTPClient().fetch(url, headers=headers)
        result = json.loads(response.body.decode("utf-8")).get("results")
        raise gen.Return(result)
    except httpclient.HTTPError as e:
        print('Exception: %s %s' % (e, url))
        raise gen.Return([])

@gen.coroutine
def save_db(collection, data):
    db[collection].insert_one(data)


def date_convert(dt):
    """
    str->datetime
    :param dt:
    """
    ptn = "(\d\d\d\d-\d\d-\d\d)T(\d\d:\d\d:\d\d)"
    pattern = re.compile(ptn)
    match = pattern.search(dt)
    s = " ".join(match.groups())
    return datetime.datetime.strptime(s, "%Y-%m-%d %H:%M:%S")


@gen.coroutine
def mainx():
    start = time.time()
    fetched = 0

    page_queue = queues.Queue()
    max_page = 1
    max_page = 29820
    for i in range(0, max_page, 20):
        url = "https://api.leancloud.cn/1.1/classes/Entry?where={}&limit=20&order=hotIndex&skip=%s"
        url = url % i
        page_queue.put(url)

    @gen.coroutine
    def worker():
        while True:
            page = yield page_queue.get()
            result = yield parse(page)
            for item in result:
                post_fields = ("tagsTitleArray", "category", "updatedAt", "viewsCount",
                               "collectionCount", "content", "objectId", "createdAt",
                               "original", "type", "title", "url", "commentsCount",
                               "originalUrl")
                post = {k: item[k] for k in post_fields if k in item}
                post['_id'] = post.pop("objectId")
                post['tags'] = post.pop("tagsTitleArray")
                post['createdAt'] = date_convert(post.pop("createdAt"))
                post['updatedAt'] = date_convert(post.pop("updatedAt"))
                user = item.get("user")
                save_db("posts", post)
                save_db("users", user)

            page_queue.task_done()



    for _ in range(concurrency):
        worker()

    yield page_queue.join()
    # yield q.join(timeout=timedelta(seconds=300))
    print('爬取%s 篇文章,总共耗时%d 秒.' % (fetched, time.time() - start))


if __name__ == '__main__':
    io_loop = ioloop.IOLoop.current()
    # io_loop.run_sync(main)
    # io_loop.run_sync(lambda: get_all_post_url(67))
    # io_loop.run_sync(lambda: get_post_data_from_url("http://python.jobbole.com/87288/", cookies))
    io_loop.run_sync(mainx)
