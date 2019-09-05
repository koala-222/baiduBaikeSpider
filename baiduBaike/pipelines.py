# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import logging
import traceback
import csv
import codecs
from baiduBaike.items import BaidubaikeItem, FileItem

class BaidubaikePipeline(object):
	def __init__(self):
		self.f = codecs.open('record1.csv', 'w', encoding = 'utf-8')
		self.writer = csv.writer(self.f, delimiter = '@')  # 使用'@'作为分隔符

	def process_item(self, item, spider):
		if isinstance(item, BaidubaikeItem):
			ID = item['ID']
			URL = item['URL']
			Place = item['Place']
			Title = item['Title']
			Prefix = item['Prefix']
			try:
				self.writer.writerow([ID, URL, Place, Title, Prefix])
			except:
				traceback.print_exc()
			return item
		
		elif isinstance(item, FileItem):
			Place = item['Place']
			Content = item['Content']
			with codecs.open(Place, 'wb', encoding = "utf-8-sig") as f:
				f.write(Content)
			return item

		else:
			logging.info('Unknown Item!')
			return item

	def close_spider(self, spider):
		self.f.close()