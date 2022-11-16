from django.contrib import admin
from .models import Courses
from django.utils.html import format_html

class CoursesAdmin(admin.ModelAdmin):
    def image_tag(self, obj):
        return format_html('<img src="{}" style="max-width:200px; max-height:200px"/>'.format(obj.img.url))
    list_display = ['image_tag','title', 'date_added']

admin.site.register(Courses, CoursesAdmin)