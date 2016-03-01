# -*- coding: utf-8 -*-
from django.contrib import admin

from main.models import *


#class CategoryAdmin(admin.ModelAdmin):
 #   list_display = ('name', 'icon')
  #  prepopulated_fields = {'slug': ('name',)}


class MainAdmin(admin.ModelAdmin):
   pass



#admin.site.register(Category, CategoryAdmin)
#admin.site.register(Main, MainAdmin)

admin.site.register(Concert, MainAdmin)
admin.site.register(Comment, MainAdmin)
