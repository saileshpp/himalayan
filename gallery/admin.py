from django.contrib import admin
from .models import Gallery
from django.utils.html import format_html


class GalleryAdmin(admin.ModelAdmin):
    def image_tag(self, obj):
        return format_html('<img src="{}" style="max-width:200px; max-height:200px"/>'.format(obj.img.url))

    list_display = ['image_tag', 'img', 'date_added']


admin.site.register(Gallery, GalleryAdmin)
