#encoding=utf-8
from django.conf.urls import url,include
from . import views

urlpatterns=[
    url(r'^$',views.index,name='index'),
    url(r'^detail/$',views.detail,name='detail'),
    url(r'^login/$',views.login,name='login'),
    url(r'^login_handle/$',views.login_handle,name='login_handle'),
    url(r'^login_out/$',views.login_out,name='login_out'),
    #对传递对变量进行命名格式为：（?P<name>正则算法）
    url(r'^(?P<pindex>\d+)/$',views.page,name='page'),
    #验证码
    url(r'^captcha/$',views.captcha_test,name='captcha'),
    url(r'^cap/$',views.cap,name='cap'),
    url(r'^jianyan/$',views.jianyan,name='jianyan'),


]