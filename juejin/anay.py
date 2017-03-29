import pandas as pd

tags_df = pd.read_csv('D:/my/crawler_html2pdf/juejin/tag.csv')

languages = ['Java', 'Python', 'Ruby', 'Swift', 'Go', 'Dart', 'Objective-C', 'C', 'C++', 'C#', 'PHP', 'JavaScript',
             'Perl', 'VB', 'R', 'MATLAB', 'Groovy', "Scala"]

lang_tags_df = tags_df[tags_df["title"].isin(languages)]

lang_tags = lang_tags[['title', 'viewsCount']]
lang_tags.drop(177, axis=0, inplace=True)

rules = {'前端': 'JavaScript'}
lang_tags['title'].replace(rules, inplace=True)

titles = lang_tags.ix[:, 0].values

lang_tags.set_index(titles, inplace=True)
lang_tags.drop('title', inplace=True, axis=1)
print(lang_tags)
lang_tags.to_csv("xx.csv")
lang_tags.plot.pie(subplots=True, figsize=(8, 4))

#
# import cufflinks as cf
#
# cf.set_config_file(world_readable=True,offline=False)
#
# pie = cf.datagen.pie()
# pie.head()


jd = ["前端", "后端", "Android", "iOS", "设计", "产品", "测试", "运营"]
