# -*- coding: utf-8 -*-
from urllib import parse
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from Biquege.items import BiqugeItem
from Biquege.utils.get_md5 import get_md5
from Biquege.items import CommonItemLoader


class BiqugeSpider(CrawlSpider):
    name = 'biquge'
    allowed_domains = ['biqudu.com']
    start_urls = ['https://www.biqudu.com/']

    rules = (
        Rule(LinkExtractor(allow=(r'xuanhuanxiaoshuo/',r'xiuzhenxiaoshuo/','dushixiaoshuo/','lishixiaoshuo/','wangyouxiaoshuo/','kehuanxiaoshuo/','nvpinxiaoshuo/','paihangbang/','wanbenxiaoshuo/'))),
        Rule(LinkExtractor(allow=r'\d+_\d+/$',unique=True), callback='parse_item'),
    )

    def parse_item(self, response):
        tmp = response.css("#fmimg > img:nth-child(1)::attr(src)").extract_first("")
        pic_path = parse.urljoin(response.url, tmp)
        loader = CommonItemLoader(item=BiqugeItem(),response=response)
        loader.add_xpath('name','//div[@id="maininfo"]/div[1]/h1/text()')
        loader.add_xpath('author','//div[@id="maininfo"]/div[1]/p[1]/text()')
        loader.add_xpath('description', '//div[@id="maininfo"]/div[2]/text()')
        loader.add_value('url', response.url)
        loader.add_value('url_object',get_md5(response.url))
        loader.add_value('pic',[[pic_path]])
        biquge_item = loader.load_item()
        return biquge_item
