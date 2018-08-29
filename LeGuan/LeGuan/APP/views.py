#coding=utf-8
from django.shortcuts import render
from django.http import HttpResponse
from models import *

#主页
def center(request):
    new_list = NewsList.objects.order_by('-id')
    new_list = new_list[0:5]
    pro_list = ProList.objects.order_by('-id')
    content = {'new_list':new_list,'pro_list':pro_list}
    return render(request,'APP/index.html',content)

def sub_msg(request):
    # cus_name = request.GET['cus_name']
    # cus_phone = request.GET.get('cus_phone')
    # cus_address = request.GET.get('cus_address')
    cus_name = request.POST['cus_name']
    cus_phone = request.POST.get('cus_phone')
    cus_address = request.POST.get('cus_address')
    print cus_name,cus_phone,cus_address
    customer = CustomerList(
        # 顾客姓名
        cus_name = cus_name,
        # 顾客联系方式
        cus_phone = cus_phone,
        # # 顾客信息
        cus_mesg = cus_address
    )
    customer.save()
    # content = {'res':'已提交，请耐心等待我们联系您～'}
    res = '已提交，请耐心等待我们联系您～'
    return HttpResponse(res)
