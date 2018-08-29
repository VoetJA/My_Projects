from django.contrib import admin
from models import *
# Register your models here.
class ProAdmin(admin.ModelAdmin):
    list_display = ['id','pro_name']

class NewAdmin(admin.ModelAdmin):
    list_display = ['date_time']

admin.site.register(NewsList,NewAdmin)
admin.site.register(CustomerList)
admin.site.register(ProList,ProAdmin)