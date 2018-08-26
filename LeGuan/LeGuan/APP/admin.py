from django.contrib import admin
from models import *
# Register your models here.
class ProAdmin(admin.ModelAdmin):
    list_display = ['id','pro_name']

admin.site.register(NewsList)
admin.site.register(CustomerList)
admin.site.register(ProList,ProAdmin)