# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class NewsItem(scrapy.Item):
    article = scrapy.Field()
    press = scrapy.Field()
    date = scrapy.Field()
    #pass
