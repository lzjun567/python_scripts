# 基于微博数据用 Python 打造一颗“心”

### 文章链接

[基于微博数据用 Python 打造一颗“心”](http://mp.weixin.qq.com/s?__biz=MjM5MzgyODQxMQ==&mid=2650366775&idx=1&sn=3fbf6f64304e528ddad88c0f6eb922e1&chksm=be9cd86389eb5175882c5666ac5ee7fe936a7b32b705244a87ce34eadfdf33f5a11236be4445&mpshare=1&scene=23&srcid=0215AAinxzHfYCxNvblNQuTf#rd)

### 准备工作
大体思路就是把微博数据爬下来，数据经过清洗加工后再分词处理，处理后的数据交给词云工具，配合科学计算工具和绘图工具制作成图像出来，涉及到的工具包有：

Requests 用于网络请求爬取微博数据，结巴分词 jieba 进行中文分词处理，wordcloud 词云处理，图片处理库 Pillow，科学计算工具 NumPy ，类似于 MATLAB 的 2D 绘图库 Matplotlib

### 工具安装
安装这些工具包时，不同系统平台有可能出现不一样的错误，wordcloud，requests，jieba 都可以通过普通的 pip 方式在线安装，
```python
pip install wordcloud
pip install requests
pip install jieba
```
在Windows 平台安装  Pillow，NumPy，Matplotlib 直接用 pip 在线安装会出现各种问题，比较推荐的一种方式是在一个叫 Python Extension Packages for Windows [1] 的第三方平台下载 相应的.whl 文件安装。可以根据自己的系统环境选择下载安装 cp27 对应 python2.7，amd64 对应 64 位系统。下载到本地后进行安装
```python
pip install Pillow-4.0.0-cp27-cp27m-win_amd64.whl
pip install scipy-0.18.0-cp27-cp27m-win_amd64.whl
pip install numpy-1.11.3+mkl-cp27-cp27m-win_amd64.whl
pip install matplotlib-1.5.3-cp27-cp27m-win_amd64.whl
```
其他平台可根据错误提示 Google 解决。也可以通过 [issue](https://github.com/lzjun567/crawler_html2pdf/issues) 在 GitHub 提交问题。

### 效果图

![iamge](./heart.jpg)

### Contact me

>作者：liuzhijun  
>微信： lzjun567  
>公众号：一个程序员的微站（id：VTtalk）  