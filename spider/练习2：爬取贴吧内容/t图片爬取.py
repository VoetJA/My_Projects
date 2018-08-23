# -*- coding:utf-8 -*-
import urllib
import urllib2
from lxml import etree

def tiebaSpider(url,begin_page,end_page):
	for page in range(begin_page,end_page+1):
		pn=(page-1)*50
		
		fullurl=url+'&pn='+str(pn) 
		# print fullurl 
		html = loadPage(fullurl)
		xml = etree.HTML(html)
		tiezi_list = xml.xpath("//div[@class='threadlist_lz clearfix']//a[@class='j_th_tit ']/@href")
		for link in tiezi_list:
			fulllink = 'http://tieba.baidu.com' + link
			loadImage(fulllink)

def loadImage(fulllink):
	request = urllib2.Request(fulllink)
	resp = urllib2.urlopen(request)
	html = resp.read()
	xml = etree.HTML(html)
	img_list = xml.xpath('//img[@class="BDE_Image"]/@src')
	for img in img_list:
		saveImg(img)

def loadPage(url):
	'''
	接受一个URL地址，并request
	'''	
	request = urllib2.Request(url)
	return urllib2.urlopen(request).read()

def saveImg(img):
	'''
	保存爬取的img
	'''
	request = urllib2.Request(img)
	image = urllib2.urlopen(request).read()
	file_name = img[-10:]
	with open(file_name,'wb') as f:
		f.write(image)
	

if __name__ == '__main__':
	kw=raw_input("请输入爬取信息的贴吧名：")
	begin_page=int(raw_input("请输入爬取的起始页："))
	end_page=int(raw_input("请输入爬取的终止页："))
	
	url="https://tieba.baidu.com/f?"
	kw=urllib.urlencode({'kw':kw})
	fullurl=url+kw
	tiebaSpider(fullurl,begin_page,end_page)