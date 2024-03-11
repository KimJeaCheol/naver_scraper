# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class stock(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    volatility = scrapy.Field()
    category = scrapy.Field()
    name = scrapy.Field()
    current_price = scrapy.Field()
    change_value = scrapy.Field()
    rate = scrapy.Field()

class finance(scrapy.Item):
    volatility = scrapy.Field()
    currency = scrapy.Field()
    current_rate = scrapy.Field()
    change_value = scrapy.Field()
    caption = scrapy.Field()
    
class stockSearchTop(scrapy.Item):
    rank_num = scrapy.Field()
    stock_name = scrapy.Field()
    search_rate = scrapy.Field()
    current_price = scrapy.Field()
    change_value = scrapy.Field()
    change_percent = scrapy.Field()
    volume = scrapy.Field()
    opening_price = scrapy.Field()
    high_price = scrapy.Field()
    low_price = scrapy.Field()
    per = scrapy.Field()
    roe = scrapy.Field()