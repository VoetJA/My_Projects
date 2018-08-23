# -*- coding:utf-8 -*-
import urllib
import urllib2

def loadPage(url,file_name):
	'''
	接受一个URL地址，并request
	'''
	print file_name + ' is loading...'
	request = urllib2.Request(url)
	return urllib2.urlopen(request).read()

def writePage(html,file_name):
	'''
	保存爬取的页面
	'''
	print file_name + 'is saving...'

	with open(file_name,'w') as f:
		f.write(html)
	print "Over   ^-^"
	print '-' * 30

def tiebaSpider(url,begin_page,end_page):
	for page in range(begin_page,end_page+1):
		pn=(page-1)*50
		file_name=str(page)+'.html'
		fullurl=url+'&pn='+str(pn) 
		# print fullurl 
		html = loadPage(fullurl,file_name)
		writePage(html,file_name)


if __name__ == '__main__':
	kw=raw_input("请输入爬取信息的贴吧名：")
	begin_page=int(raw_input("请输入爬取的起始页："))
	end_page=int(raw_input("请输入爬取的终止页："))
	
	url="https://tieba.baidu.com/f?"
	kw=urllib.urlencode({'kw':kw})
	fullurl=url+kw
	tiebaSpider(fullurl,begin_page,end_page)
	
