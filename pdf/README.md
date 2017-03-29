#Python 爬虫：把廖雪峰的教程转换成 PDF 电子书

### 系统要求
python3.4以上版本, 不支持python2.x


### 准备工具

requests、beautifulsoup 是爬虫两大神器，reuqests 用于网络请求，beautifusoup 用于操作 html 数据。有了这两把梭子，干起活来利索。scrapy 这样的爬虫框架我们就不用了，这样的小程序派上它有点杀鸡用牛刀的意思。此外，既然是把 html 文件转为 pdf，那么也要有相应的库支持， wkhtmltopdf 就是一个非常的工具，它可以用适用于多平台的 html 到 pdf 的转换，pdfkit 是 wkhtmltopdf 的Python封装包。首先安装好下面的依赖包

```python
pip install requests
pip install beautifulsoup4
pip install pdfkit
```

### 安装 wkhtmltopdf
Windows平台直接在 [http://wkhtmltopdf.org/downloads.html](http://wkhtmltopdf.org/downloads.html) 下载稳定版的 wkhtmltopdf 进行安装，安装完成之后把该程序的执行路径加入到系统环境 $PATH 变量中，否则 pdfkit 找不到 wkhtmltopdf 就出现错误 “No wkhtmltopdf executable found”。Ubuntu 和 CentOS 可以直接用命令行进行安装

```shell
$ sudo apt-get install wkhtmltopdf  # ubuntu
$ sudo yum intsall wkhtmltopdf      # centos
```

### 运行
```python
python crawler.py
```

### 效果图
![image](./crawer-pdf.png)

### 常见问题

1. SyntaxError: Missing parentheses in call to 'print'
    
    beautifulsoup3不支持python2,所以下载beautifulsoup是要指定 beautifusoup4
2. 如果是使用PyCharm开发, 那么运行的时候要在shell/cmd 窗口执行脚本, 直接在Pycharm中运行会找不到 wkhtmltopdf命令

3. 生成的PDF文件可以在公众号回复『pdf』下载

### 更新记录

* 2017-2-21: 对代码进行了全面的重构,可扩展, 子类爬虫只需实现 `parse_menu`和`parse_body`方法就可以实现HTML转换PDF的逻辑


### Contact me

>作者：liuzhijun  
>微信： lzjun567  
>公众号：Python之禅（id：VTtalk）


