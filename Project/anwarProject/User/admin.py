import re
from django.contrib import admin
from .models import user,post
# Register your models here.

'''class userAdmin(admin.ModelAdmin):
    list_display=('first_name','last_name','email','password','username')


class postAdmin(admin.ModelAdmin):
    list_display=('user','text','created_at','updated_at')'''

admin.site.register(user)
admin.site.register(post)
