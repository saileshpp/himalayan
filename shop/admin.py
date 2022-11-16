from django.contrib import admin
from .models import *
from django.utils.html import format_html


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    def image_tag(self, obj):
        return format_html('<img src="{}" style="max-width:200px; max-height:200px"/>'.format(obj.img.url))
    list_display = ['image_tag', 'title', 'highlight', 'date_added']


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['name', 'date_added', 'email']

    # def has_add_permission(self, request, obj=None):
    #     return False


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'number', 'date_added']

    def has_add_permission(self, request, obj=None):
        return False
