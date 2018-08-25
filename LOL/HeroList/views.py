#coding=utf-8
from django.shortcuts import render,redirect
from django.http import HttpResponse
from models import *
from django.core.paginator import Paginator
from captcha.captcha import Captcha
from django.core.cache import cache

#练习第三方模板接口使用
def captcha_test(request):
    cache.delete('name')
    captcha = Captcha.instance()
    name,text,image = captcha.generate_captcha()
    cache.set('name',text,600)
    return HttpResponse(image,'image/jpeg')

def cap(request):

    return render(request,'HeroList/captcha.html')

def jianyan(request):
    text1 = request.POST['text']
    text2 = cache.get('name')
    cache.delete('name')
    if text1 == text2:
        return HttpResponse('ok')
    else:
        return HttpResponse('no')

def index(request):
# 从数据库中对英雄对象进行提取并放置于list列表中，通过context传输至Html页面使用
    # list = HeroInfo.objects.all()
    # context = {'list':list}
    # return render(request,'HeroList/index.html',context)

#从session中接受参数，并对其进行判断/赋值
    if request.session.get('uname'):
        uname = request.session.get('uname')
        context = {'uname': uname}
    else:
        context = {'uname':'您尚未登录'}
    return render(request,'HeroList/index.html',context)

def page(request,pindex):
#对英雄列表进行分页操作
    list = HeroInfo.objects.all()
    p = Paginator(list,5)
    if pindex == '':
        pindex = 1
    pindex = int(pindex)
    list2 = p.page(pindex)
    plist = p.page_range
    return render(request,'HeroList/page.html',{'list':list2,'plist':plist,'pindex':pindex})

def detail(request):
    return render(request,'HeroList/detail.html')

def login(request):
    a = request.GET.get('next')
    request.session['a']=a
    return render(request,'HeroList/login.html')

def login_handle(request):
    request.session['uname'] = request.POST['uname']
    # return redirect(reverse('main:index'))
    # 可简写如下
    return redirect('main:index')


def login_out(request):
    #删除session中保存的内容
    #del request.session['uname']
    #request.session.clear()
    request.session.flush()
    # return redirect(reverse('main:index'))
    # 可简写如下
    return redirect('main:index')