#coding=utf-8
from django.contrib import admin
from models import HeroArea, HeroInfo

#以块形式嵌入
# class HeroInfoInline(admin.StackedInline):
#     model = HeroInfo
#     extra = 3

#以表格的形式嵌入
class HeroInfoInline(admin.TabularInline):
    model = HeroInfo
    #表示一次加入的数量
    extra = 3


class HeroListShow(admin.ModelAdmin):
    list_display = ['id','h_name','gender']


class Gender(admin.ModelAdmin):
    inlines = [HeroInfoInline]
    list_display = ['id','h_title']

admin.site.register(HeroArea,Gender)
admin.site.register(HeroInfo,HeroListShow)
