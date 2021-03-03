from django.contrib import admin
from .models import itemsPost,saveOrder, requestS, set

# Register your models here.
# admin.site.register(itemsPost)

@admin.register(itemsPost)
class postAdmin(admin.ModelAdmin):
    list_display = ( 'itemName','id','rate')
    list_filter	= ('techSpecs','make','UOM')
    search_fields = ('itemName', 'itemCode''rate')
    ordering = ('rate','itemName','itemCode')

@admin.register(saveOrder)
class toOrderAdmin(admin.ModelAdmin):
    list_display =  ('code', 'id' ,'quantity')
    search_fields = ('code','quantity')
    list_filter	= ('center',)

@admin.register(requestS)
class toRequestS(admin.ModelAdmin):
    list_display = ('itemName', 'id','rate','documentName', 'documentDate')
    list_filter	= ('make','UOM')
    search_fields = ('itemName', 'itemCode''rate')
    ordering = ('rate','documentDate')

@admin.register(set)
class toSet(admin.ModelAdmin):
    list_display =  ('companyName','id','dN', 'dD')
    search_fields = ('companyName','dN', 'dD')
    list_filter	= ('dN','dD')   
    ordering = ('dD',)
