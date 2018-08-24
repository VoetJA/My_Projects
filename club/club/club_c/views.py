#encoding=utf-8
from django.shortcuts import render,redirect,HttpResponse
from models import *
# from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_page


#主页
# @cache_page(60*5)  这个装饰器可以缓存这个视图，传入参数是时间（秒）
def index(request):
    palte_list = palte.objects.all()
    artical_list = Articals.objects.order_by('-id')
    content = {'palte_list':palte_list,'artical_list':artical_list}
    return render(request,'club_c/index.html',content)

#转到登录页
def login_page(request):
    nex_url = request.GET.get('next', '/')
    request.session['nex_url']=nex_url
    return render(request,'club_c/login.html')


#用户认证
def auth_view(request):
    username = request.POST["username"] # 获取用户名
    password = request.POST["password"]  # 获取用户的密码
    # next_url = request.get.path()
    # nex_url=request.GET.get('next')
    # print(nex_url)
    user = authenticate(username=username, password=password)  # 验证用户名和密码，返回用户对象

    if user is not None:  # 如果用户对象存在
        login(request, user)  # 用户登陆
        # nex_url = request.GET.get('next', '/')
        nex_url = request.session.get('nex_url')
        # return redirect('main:index')
        return redirect(nex_url)

    else:
        return HttpResponse("用户名或密码错误")

#用户注销
def logout_view(request):

    logout(request)  # 注销用户
    nex_url = request.session.get('next', '/')
    return redirect(nex_url)
    # return redirect('main:index')

#板块内容分类展示
def showp(request):
    # , palte_id, sort_id
    palte_id=request.GET.get("palte")
    sort_id=request.GET.get('sort')
    palte_list = palte.objects.all()
    if palte_id == '0' or palte_id == '':
        artical_list = Articals.objects.all()
    else:
        artical_list = Articals.objects.filter(in_palte__id=palte_id)
    if sort_id=='1':
        artical_list = artical_list.order_by('-id')
    else :
        artical_list = artical_list.order_by('-click_num')
    content = {'palte_id':palte_id,'palte_list':palte_list,'artical_list':artical_list,'sort':sort_id}
    return render(request,'club_c/showPage.html',content)


#创作新帖子，登录验证装饰器
@login_required
def creartical(request):
    palte_list = palte.objects.all()
    content = {'palte_list':palte_list}
    return render(request,'club_c/crartical.html',content)

#提交帖子各类信息
def creartical_handler(request):
    title = request.POST['title']
    content = request.POST['content']
    in_palte = request.POST['in_palte']
    in_palte = palte.objects.get(pk=in_palte)
    user = clubUser.objects.get(user = request.user)
    print(user)
    Articals.objects.create(
        title=title,
        # 帖子内容
        content = content,
        # 作者
        author = user,
        # 所属板块
        in_palte = in_palte
    )
    return redirect('main:index')

#浏览帖子内容页
def artical(request,artical_id):

    palte_list = palte.objects.all()
    artical = Articals.objects.get(id=artical_id)
    ap_id = artical.in_palte.id
    artical.click_num += 1
    artical.save()
    # url = request.get_all_path()
    content = {'palte_list': palte_list, 'artical': artical,'ap_id':ap_id}
    return render(request,'club_c/content.html',content)

#转到注册页
def register(request):
    next_url = request.GET.get('next')
    request.session['next_url']=next_url
    return render(request,'club_c/register.html')

#注册新用户
def register_handler(request):
    # next_url = request.session.get('next_url','/')
    username = request.POST['username']
    password = request.POST['password']
    user = User.objects.create_user(username=username, password=password)
    user.save()
    clubUser.objects.create(
        user = user
    )

    return redirect('main:login_page')