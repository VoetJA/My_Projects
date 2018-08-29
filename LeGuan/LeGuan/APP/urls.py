from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.center,name='center'),
    url(r'^sub_msg/$',views.sub_msg,name='sub_msg'),
]