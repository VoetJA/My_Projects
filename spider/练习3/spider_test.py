# import urllib2
# from lxml import etree
# import threading
# # import requests

# class myThreading(threading.Thread):
# 	"""docstring for myThreading"""
# 	def __init__(self):
# 		super(myThreading, self).__init__()
		
	
# 	def run(self):
# 		self.downLink()

# 	def downLink(self):	
# 		requests = urllib2.Request(url,headers = headers)
# 		resp = urllib2.urlopen(requests)
# 		html = resp.read()
# 		# html = requests.get(url,headers = headers).text
# 		xhtml = etree.HTML(html)
# 		img_list = xhtml.xpath('//a[contains(@class,"recom")]/@href')
# 		for link in img_list:
# 			self.saveImg(link)

# 	def saveImg(self,link):
# 			imgurl = 'http://wx.cubejoy.com/' + link
# 			# print(imgurl)
# 			requests = urllib2.Request(url,headers = headers)
# 			resp = urllib2.urlopen(requests)
# 			img = resp.read()
# 			# img = requests.get(imgurl,headers = headers).content
# 			img_name = link[-7:]
# 			with open(img_name,'wb') as f:
# 				f.write(img)

# if __name__ == '__main__':
# 	url = 'https://wx.cubejoy.com/pic.html'
# 	headers =  {"User-Agent" : "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;"}
# 	mytrd = myThreading()
# 	mytrd.start()

# import urllib2
from lxml import etree
import threading
import requests

class myThreading(threading.Thread):
	"""docstring for myThreading"""
	def __init__(self):
		super(myThreading, self).__init__()
		
	
	def run(self):
		self.downLink()

	def downLink(self):	
		# requests = urllib2.Request(url,headers = headers)
		# resp = urllib2.urlopen(requests)
		# html = resp.read()
		html = requests.get(url,headers = headers).text
		xhtml = etree.HTML(html)
		img_list = xhtml.xpath('//a[contains(@class,"recom")]/@href')
		for link in img_list:
			self.saveImg(link)

	def saveImg(self,link):
			imgurl = 'http://wx.cubejoy.com/' + link
			# print(imgurl)
			# requests = urllib2.Request(url,headers = headers)
			# resp = urllib2.urlopen(requests)
			# img = resp.read()
			img = requests.get(imgurl,headers = headers).content
			img_name = link[-7:]
			with open(img_name,'wb') as f:
				f.write(img)

if __name__ == '__main__':
	url = 'https://wx.cubejoy.com/pic.html'
	headers =  {"User-Agent" : "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;"}
	mytrd = myThreading()
	mytrd.start()