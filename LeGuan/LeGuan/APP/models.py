#coding=utf-8
from django.db import models


#新闻表
class NewsList(models.Model):
    #创建日期
    date_time = models.DateTimeField(auto_now_add=True,verbose_name='日期')
    #内容
    new_content = models.TextField(verbose_name='新闻内容')

    class Meta:
        verbose_name_plural = '最新新闻'
    def __str__(self):
        return self.new_content.encode('utf-8')

#产品表
class ProList(models.Model):
    #产品名称
    pro_name = models.CharField(max_length=30,verbose_name='产品名称')
    #产品图片
    pro_img = models.ImageField(upload_to='ProIMg/',verbose_name='产品图片')
    #产品介绍
    pro_txt = models.TextField()
    def __str__(self):
        return self.pro_name.encode('utf-8')
    class Meta:
        verbose_name_plural = '产品'

#意向用户
class CustomerList(models.Model):
    #顾客姓名
    cus_name = models.CharField(max_length=10,verbose_name='用户名')
    #顾客联系方式
    cus_phone = models.CharField(max_length=11,verbose_name='联系方式')
    #顾客信息
    cus_mesg = models.CharField(max_length=255,verbose_name='联系信息')

    def __str__(self):
        return self.cus_name.encode('utf-8')
    class Meta:
        verbose_name_plural = '意向用户'