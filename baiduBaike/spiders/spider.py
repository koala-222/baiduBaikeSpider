import logging
import scrapy
import codecs
import urllib.parse
import re
import os
from bs4 import BeautifulSoup
from baiduBaike.items import BaidubaikeItem, FileItem


class MySpider(scrapy.spiders.CrawlSpider):
	name = "baiduBaike"
	allowed_domains = ["baike.baidu.com"]
	savePath = "./pages1/"
	startPage = 1
	endPage = 1000000
	div = 10000  # 子文件夹大小
	start_urls = ["http://baike.baidu.com"]
	urlPattern = "http://baike.baidu.com/view/{0}.htm"


	def parse(self, response):
		#self.extrc(response)
		for i in range(self.startPage, self.endPage):
			url = self.urlPattern.format(i)
			req = scrapy.http.request.Request(url, callback = self.extrc)
			req.meta['id'] = i
			yield req


	def extrc(self, response):
		url = urllib.parse.unquote(response.url).strip()
		soup = BeautifulSoup(response.body, 'lxml')
		
		bodyWrapper = soup.find('div', attrs={'class': 'body-wrapper'})
		tl = soup.find("dd", attrs = {"class": "lemmaWgt-lemmaTitle-title"})
		if bodyWrapper is None or tl is None:
			req = scrapy.http.request.Request(url, callback = self.extrc)
			req.meta['id'] = response.meta['id']
			yield req
			return

		sublemma_list = bodyWrapper.find("div", attrs={"class": "lemmaWgt-subLemmaListTitle"})
		if not sublemma_list:
			filename = re.sub("[/?&=#.\"'\\:*<>\|]", "_", url.split("/", 4)[-1])
			urlid = response.meta['id']
			subdir = str(urlid // self.div)  # 子文件夹
			try:
				os.makedirs(self.savePath + subdir)
			except:
				pass
			PLACE = self.savePath + subdir + '/' + filename

			#写入文件
			fitem = FileItem()
			fitem['Place'] = PLACE
			fitem['Content'] = str(bodyWrapper)
			yield fitem
			
			#写入数据库
			title = tl.find("h1").get_text().strip()
			h2 = tl.find("h2")
			if h2:
				subtitle = h2.get_text().strip()
			else:
				subtitle = ""
			item = BaidubaikeItem()
			item['ID'] = urlid
			item['URL'] = url
			item['Place'] = PLACE
			item['Title'] = title + subtitle
			item['Prefix'] = title
			yield item
