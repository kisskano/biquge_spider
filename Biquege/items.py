# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import Compose,TakeFirst
from scrapy.loader import ItemLoader


def delstr(value):
    return value[0].replace('作    者：','')


def desrepair(value):
    list = []
    for i in value:
        list.append(i.strip())
    return '<br/>'.join(list)



class CommonItemLoader(ItemLoader):
    default_output_processor = TakeFirst()
    pass


class BiqugeItem(scrapy.Item):
    name = scrapy.Field()
    author = scrapy.Field(input_processor = Compose(delstr))
    description = scrapy.Field(input_processor = Compose(desrepair))
    url = scrapy.Field()
    url_object = scrapy.Field()
    pic = scrapy.Field()
    pic_url = scrapy.Field()

    def insert_sql(self):
        # print(self['description'])
        i_sql = "insert into novel values(%s,%s,%s,%s,%s,%s,%s)on duplicate key update name=values(name),description=values (description)"
        params = (self['name'],self['author'],self['description'],self['url'],self['url_object'],self['pic'][0],self['pic_url'])
        return i_sql,params

