#coding=utf-8
from django.shortcuts import render
from models import *

#主页
def center(request):
    new_list = NewsList.objects.order_by('-id')
    # new_list = new_list[0:4]
    pro_list = ProList.objects.filter()
    content = {'new_list':new_list,'pro_list':pro_list}
    return render(request,'APP/index.html',content)
