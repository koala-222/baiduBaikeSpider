# 百度百科爬虫

利用Scrapy1.6框架，爬取全部的百度百科页面。

爬取结果通过pipeline写入磁盘文件。



运行环境：

- scrapy1.6
- python3.7



运行命令：

```shell
scrapy crawl baiduBaike 
```



**需要自己实现util.py中获取代理的模块**

