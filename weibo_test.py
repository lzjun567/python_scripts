# -*- coding:utf-8 -*-
import requests

cookies = {


}

import MySQLdb


def crawler_weibo():
    db = MySQLdb.connect("localhost", "root", "vancouver", "bao_db", charset="utf8")
    for i in range(1, 102):
        try:
            url = "http://m.weibo.cn/index/my?format=cards&page=%s" % i
            response = requests.get(url, cookies=cookies)
            data = response.json()[0]
            texts = data.get("card_group")
            for text in texts:
                content = text.get("mblog").get("text")
                print content
                content = content.encode("utf-8")
                import re
                pattern = "<a .*?/a>|<i .*?/i>"
                content = re.sub(pattern, "", content)
                content = content.replace("//:","").replace("转发微博","").replace("Repost","").replace("，","").replace("？","").replace("。","").replace("、","")
                db.cursor().execute("insert into test_weibo (text) VALUES (%s)", content)
            db.commit()
        except Exception as e:
            print e
    db.close()


def generate_img():
    global wordcloud
    import pandas as pd
    df = pd.read_csv('weibo2.csv')
    import matplotlib.pyplot as plt
    from wordcloud import WordCloud, STOPWORDS
    words = ' '.join(df['text'])
    print (type(words))
    # print df['text']
    #
    # join tweets to a single string
    # remove URLs, RTs, and twitter handles
    import jieba
    l = []

    for word in words.split():
        l.extend(fine(word))
    no_urls_no_tags = " ".join(l)
    print 'xxxxxxx'
    from scipy.misc import imread

    twitter_mask = imread('./HeatherT-heart-vine-mask.jpg', flatten=True)
    wordcloud = WordCloud(
        font_path='msyh.ttc',
        stopwords=STOPWORDS,
        background_color='black',
        width=1800,
        height=1400,
        mask=twitter_mask
    ).generate(no_urls_no_tags)
    plt.imshow(wordcloud)
    plt.axis('off')
    plt.savefig('./my_twitter_wordcloud_13.png', dpi=300)
    plt.show()

def fine(content):
    import jieba
    import jieba.analyse
    jieba.analyse.set_stop_words("stop_word.txt")
    tags = jieba.analyse.extract_tags(content, topK=20)
    return tags


if __name__ == '__main__':
    generate_img()
    # s = "<i href='/n/周源'>@周源</i>知乎专栏文章为啥找不到收藏的入口呢 <a href='/n/周源'>@周源</a> ​​​"
    # import re
    #
    # pattern = "<a .*?/a>|<i .*?/i>"
    # print re.sub(pattern, "", s)
    # crawler_weibo()
    # import jieba
    # import jieba.analyse
    # jieba.analyse.set_stop_words("stop_word.txt")
    # content = u"""红包最暖心~我在王思聪 的红包中抽到了 提供的“快的打车6元红包”快来试试手气你与幸福之间只有一个红包的距离！ ​​​"""
    # tags = jieba.analyse.extract_tags(content, topK=20)
    # print " ".join(tags)
    # seg_list = jieba.cut(content, cut_all=False)
    # s = []
    # for seg in seg_list:
    #     if seg not in (u"的",u"了",u"和",u"是",u"就",u"都",u"而",u"及",u"或", u"我", u"来",u"一个",u"只有",u"之间"):
    #         s.append(seg)
    # print " ".join(s)
    # print("Default Mode: " + "/ ".join(seg_list))  # 精确模式
    # pass

    # crawler_weibo()

# print response.content
