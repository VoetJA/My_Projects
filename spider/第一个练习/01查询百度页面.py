#-*- coding:utf-8 -*-
import urllib2
import urllib
url='http://www.baidu.com/s'
keyword=raw_input("请输入要查询的关键词：")
wd={'wd':keyword}
wd=urllib.urlencode(wd)
fullurl=url+'?'+wd
zj_headers={'User-Agent':' Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}

request=urllib2.Request(fullurl,headers=zj_headers)

response=urllib2.urlopen(request)

html=response.read()

print fullurl

