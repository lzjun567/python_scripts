# -*- coding:utf-8 -*-
import pkuseg
from collections import Counter
import pprint

content = []
with open("yanjiang.txt", encoding="utf-8") as f:
    content = f.read()

lexicon = ['小程序', '朋友圈', '公众号']  #
seg = pkuseg.pkuseg(user_dict=lexicon)  # 加载模型，给定用户词典
text = seg.cut(content)

stopwords = []

with open("stopword.txt", encoding="utf-8") as f:
    stopwords = f.read()

new_text = []

for w in text:
    if w not in stopwords:
        new_text.append(w)

counter = Counter(new_text)
pprint.pprint(counter.most_common(50))
