# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SinaspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # pass

    parentTitle = scrapy.Field()
    parentUrls = scrapy.Field()

    subTitle = scrapy.Field()
    subUrls = scrapy.Field()

    subFilename = scrapy.Field()

    sonUrls = scrapy.Field()

    head = scrapy.Field()
    content = scrapy.Field()