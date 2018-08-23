import scrapy
from itcast.items import ItcastItem

class ItcastSpider(scrapy.Spider):
	name = 'Itcast'
	allowd_domains = ['http://www.itcast.cn/']
	start_urls = ['http://www.itcast.cn/channel/teacher.shtml#aandroid']

	def parse(self,response):
		
		techer_list=response.xpath('//div[@class="li_txt"]')
		list1=[]
		for each in techer_list:
			item=ItcastItem()
			name=each.xpath('./h3/text()').extract()
			title=each.xpath('./h4/text()').extract()
			info=each.xpath('./p/text()').extract()
			# print(title[0])
			# item['name']=name[0].encode('gbk')
			# item['title']=title[0].encode('gbk')
			# item['info']=info[0].encode('gbk')
			item['name']=name[0]
			item['title']=title[0]
			item['info']=info[0]
			list1.append(item)
		return list1
 