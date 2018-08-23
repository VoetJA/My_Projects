from django.contrib import admin
from club_c.models import *

# Register your models here.

class AritcalShow(admin.ModelAdmin):
    list_display = ['id','title','create_time','author','in_palte']

# class ClubuserShow(admin.ModelAdmin):
#     list_display = ['user.username']

class PalteShow(admin.ModelAdmin):
    list_display = ['id','name']


admin.site.register(clubUser)
admin.site.register(palte,PalteShow)
admin.site.register(Articals,AritcalShow)