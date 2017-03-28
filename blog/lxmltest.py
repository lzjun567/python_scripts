# encoding: utf-8
__author__ = 'liuzhijun'

from lxml import etree

text = '''

<div class="col">
    <div class="footer-title">Sitemap</div>
    <ul class="list-unstyled">
        <li><a href="https://foofish.net/categories.html">分类</a></li>
        <li><a href="https://foofish.net/tags.html">标签</a></li>
        <li><a href="https://foofish.net/pages/about.html">关于</a></li>
        <li><a href="https://foofish.net/feeds/all.atom.xml" type="application/atom+xml" rel="alternate"></a></li>
        <li><a href="https://foofish.net/feeds/rss.xml" type="application/rss+xml" rel="alternate">RSS</a></li>
    </ul>
</div>
'''
html = etree.XML(text)

html = etree.fromstring(text)

for i in html.xpath("//@class"):
    print(i)
    # print(etree.tostring(i))

# print(etree.tostring(html.xpath("//div")))
#
#
# result = etree.tostring(html)
# print(result)
#
#
# # 构建一个 root 元素节点
#
# root = etree.Element("root")
# print(root)
#
# # tag是元素节点的名称
# print(root.tag)
#
#
# # 添加子节点元素
#
# ch1 = etree.SubElement(root, "ch1")
# ch2 = etree.SubElement(root, "ch2")
# ch3 = etree.SubElement(root, "ch3")
#
# # 输出xml内容
# print(etree.tostring(root))
#
# # 删除子节点
#
# root.remove(ch1)
# print(etree.tostring(root))
#
# # 清除所有节点(除根节点外)
# #root.clear()
# #print(etree.tostring(root))
#
# # 像列表一样操作元素
# ch = root[0]
# print(ch.tag)
# print(len(root))
# print(ch.getparent())
#
# for ch in root:
#     print(ch.tag)
#
#
# # 创建属性(像字典一样)
# root = etree.Element("root", height="100")
# print(etree.tostring(root))
#
# # 获取属性值
# print(root.get("height"))
#
# # 设置属性
# root.set("size", "200")
# print(etree.tostring(root))
#
# # root.keys
# # root.items
#
# # 元素的文本操作
# print(root.text)
# root.text = "hellworld"
# print(etree.tostring(root))
#
#
# http://lxml.de/tutorial.html#the-element-class