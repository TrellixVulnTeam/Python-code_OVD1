# -*- coding: utf-8 -*-
import scrapy
from ..items import SinaspiderItem
import os

class SinaSpider(scrapy.Spider):
    name = 'sina'
    allowed_domains = ['sina.com.cn']
    start_urls = ['http://news.sina.com.cn/guide']

    def parse(self, response):
    	items = []

    	parentUrls = response.xpath('//div[@id="tab01"]//h3/a/@href').extract()
    	parentTitle = response.xpath('//div[@id="tab01"]//h3/a/text()').extract()

    	subUrls = response.xpath('//div[@id="tab01"]//ul/li/a/@href').extract()
    	subTitle = response.xpath('//div[@id="tab01"]//ul/li/a/text()').extract()

        # for i in range(0, len(parentTitle)):
    	for i in range(0, 1):
    		parentFilename = './Data/' + parentTitle[i]

    		if (not os.path.exists(parentFilename)):
    			os.makedirs(parentFilename)

    		for j in range(0, len(subUrls)):
    			item = SinaspiderItem()

    			item['parentTitle'] = parentTitle[i]
    			item['parentUrls'] = parentUrls[i]

    			if_belong = subUrls[j].startswith(item['parentUrls'])

    			if (if_belong):
    				subFilename = parentFilename + '/' + subTitle[j]

    				if (not os.path.exists(subFilename)):
    					os.makedirs(subFilename)

    				item['subUrls'] = subUrls[j]
    				item['subTitle'] = subTitle[j]
    				item['subFilename'] = subFilename

    				items.append(item)
    	for item in items:
    		yield scrapy.Request(url = item['subUrls'], meta={'meta_1': item}, callback=self.second_parse)


    def second_parse(self, response):
    	meta_1 = response.meta['meta_1']

    	sonUrls = response.xpath('//a/@href').extract()
    	items = []
    	for i in range(0, len(sonUrls)):
    		if_belong = sonUrls[i].endswith('.shtml') and sonUrls[i].startswith(meta_1['parentUrls'])

    		if (if_belong):
    			item = SinaspiderItem()

    			item['parentTitle'] = meta_1['parentTitle']
    			item['parentUrls'] = meta_1['parentUrls']
    			item['subUrls'] = meta_1['subUrls']
    			item['subTitle'] = meta_1['subTitle']
    			item['subFilename'] = meta_1['subFilename']
    			item['sonUrls'] = sonUrls[i]

    			items.append(item)
    	for item in items:
    		yield scrapy.Request(url=item['sonUrls'], meta={'meta_2': item}, callback=self.detail_parse)

    def detail_parse(self, response):
    	item = response.meta['meta_2']

    	content = ''
    	head = response.xpath('//h1[@id="artibodyTitle"]/text()')
    	content_list = response.xpath('//div[@id="artibody"]/p/text()').extract()

    	for content_one in content_list:
    		content += content_one

    	item['head'] = head
    	item['content'] = content

    	yield item
