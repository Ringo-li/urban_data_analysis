# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ArticleItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    abstract = scrapy.Field()
    author = scrapy.Field()
    author_num = scrapy.Field()
    ins = scrapy.Field()
    date = scrapy.Field()
    keywords = scrapy.Field()
    fund = scrapy.Field()
    cite = scrapy.Field()
    # pass
