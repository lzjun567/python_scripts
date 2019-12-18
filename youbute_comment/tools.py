"""
词频统计
"""
import jieba

result = jieba.cut("我爱中国北京大学", cut_all=True)
for word in result:
	print(word)

import jieba.analyse

result = jieba.analyse.extract_tags("机器学习，需要一定的数学基础，需要掌握的数学基础知识特别多，"
                                    "如果从头到尾开始学，估计大部分人来不及，机器学习我建议先学习最基础的数学知识机器学习机器学习",
                                    topK=5)
import pprint

pprint.pprint(result)
