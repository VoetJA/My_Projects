#coding=utf-8
from django.db import models


class HeroArea(models.Model):
    h_title = models.CharField(max_length=20)
    def __str__(self):
        return self.h_title.encode('utf8')


class HeroInfo(models.Model):
    h_name = models.CharField(max_length=20)
    h_gender = models.BooleanField(default=True)
    h_gun = models.CharField(max_length=20)
    h_area = models.ForeignKey(HeroArea)
    def __str__(self):
        return self.h_name.encode('utf-8')
    def gender(self):
        if self.h_gender:
            return '男'
        else:
            return '女'