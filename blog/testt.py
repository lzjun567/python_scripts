# encoding: utf-8
__author__ = 'liuzhijun'

import urllib.request as urllib

from collections import deque
def cache(func):
    saved = {}

    def wrapper(url):
        if url in saved:
            return saved[url]
        else:
            page = func(url)
            saved[url] = page
            return page

    return wrapper


def web_lookup(url, saved={}):
    if url in saved:
        return saved[url]
    page = urllib.urlopen(url).read()
    saved[url] = page
    return page


@cache
def web_lookup(url):
    return urllib.urlopen(url).read()


def main():
    import jieba
    seg_list = jieba.cut("最实用的微信小程序大全，持续更新中...", cut_all=False)
    print("Default Mode: " + "/ ".join(seg_list))  # 精确模式


if __name__ == '__main__':
    main()
