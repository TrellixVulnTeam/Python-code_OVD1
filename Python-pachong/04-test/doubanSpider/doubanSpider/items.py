# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanspiderItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()

    posterLink = scrapy.Field()

    posterPath = scrapy.Field()

    bd = scrapy.Field()

    star = scrapy.Field()

    quote = scrapy.Field()
