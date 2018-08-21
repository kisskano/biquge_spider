# _*_ coding: utf-8 _*_
__author__ = 'Thomas'
__date__ = '2018/8/21 08:30'
import os,sys
from scrapy.cmdline import execute
sys.path.append(os.path.dirname(__file__))
execute(['scrapy','crawl','biquge'])