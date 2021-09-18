import json
import re
import time
from http.cookies import SimpleCookie
from imageio import imread
from wordcloud import WordCloud
import jieba.analyse

print(__file__)
def word_segment(text):
    # 分词处理
    jieba.analyse.set_stop_words("./stopwords.txt")
    words = jieba.cut(text)
    from collections import Counter
    result = Counter(words).most_common(20)
    print(result)

    tags = jieba.analyse.extract_tags(text, topK=20)
    print(tags)


if __name__ == '__main__':
    text = open("text.txt", encoding="utf-8").read()
    word_segment(text)
    pass


def word_cloud(texts):
    """
    根据文本生成词云图片
    """
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


def cookie(s):
    from http.cookies import SimpleCookie

    rawdata = s
    cookie = SimpleCookie()
    cookie.load(rawdata)

    # Even though SimpleCookie is dictionary-like, it internally uses a Morsel object
    # which is incompatible with requests. Manually construct a dictionary instead.
    cookies = {}
    for key, morsel in cookie.items():
        cookies[key] = morsel.value
    return cookie


def format_duration(duration):
    """
    格式化时长
    :param duration 毫秒
    """

    total_seconds = int(duration / 1000)
    minute = total_seconds // 60
    seconds = total_seconds % 60
    return f'{minute:02}:{seconds:02}'