# _*_ coding: utf-8 _*_
__author__ = 'Thomas'
__date__ = '2018/8/21 10:07'
import hashlib
def get_md5(url):
    if isinstance(url,str):
        url =url.encode('utf-8')
    m = hashlib.md5()
    m.update(url)
    return m.hexdigest()
