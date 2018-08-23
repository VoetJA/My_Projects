#coding=utf-8
import urllib2
import re

class Spider:
	#内部定义爬取的第一页和设置开关
	def __init__(self):
		self.page=1
		self.switch=True

	#下载页面	
	def down(self):
		url='http://www.neihan8.com/article/list_5_'+str(self.page)+'.html'
		headers={"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}
		request=urllib2.Request(url,headers=headers)
		resp=urllib2.urlopen(request)
		html=resp.read()
		deal_page(html)		

	
	 #处理页面，去除页面无用内容
	def deal_page(self,html):
		pattern = re.compile('<div>\sclass="<div\sclass="f18 mb20">(.*?)</div>',r.S)
		context = pattern.findall(html)
		for dz in context:
			dz=dz.replace('<p>','').replace('</p>','')
			self.save_page(dz)

	def save_page(self,dz):
		with open('duanzi.txt','a') as f:
			f.write(dz)


	#总开关，负责是否继续进行爬取
	def control(self):
		while self.switch:
			self.down()
			self.page+=1
			cont = raw_print('如果继续爬取请按ENter，返回请输入quit：')
			if cont == 'quit':
				self.switch=False
		print('已退出，谢谢使用！')

if __name__ == '__main__':
	sp=Spider()
	sp.control()
	