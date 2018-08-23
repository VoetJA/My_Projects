#encoding=utf-8
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^artical/(\d+)/$',views.artical,name='artical'),
    url(r'^showp/$',views.showp,name='showp'),
   #转到登录页
    url(r'login/$',views.login_page,name='login_page'),
    #登录验证
    url(r'auth_view/$',views.auth_view,name='auth_view'),
    #登出验证
    url(r'logout/$', views.logout_view, name='logout'),
    #发帖
    url(r'creartical/$', views.creartical, name='creartical'),
    #提交帖子
    url(r'creartical_handler/$', views.creartical_handler, name='creartical_handler'),
    #注册
    url(r'register/$', views.register, name='register'),
    #提交注册信息
    url(r'register_handler/$', views.register_handler, name='register_handler'),



    ]