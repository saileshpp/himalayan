from django.contrib import admin
from blog__app.models import *
from home.models import *
from django.utils.html import format_html


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'author']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['author', 'blog', 'date_added', 'email']

    def has_add_permission(self, request, obj=None):
        return False


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email']

    def has_add_permission(self, request, obj=None):
        return False


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ['title']

    def has_delete_permission(self, request, obj=None):
        return False


class HomeSliderAdmin(admin.ModelAdmin):
    def image_tag(self, obj):
        return format_html('<img src="{}" style="max-width:200px; max-height:200px"/>'.format(obj.image.url))

    list_display = ['image_tag', 'image']


admin.site.register(HomeSlider, HomeSliderAdmin)


@admin.register(OurTeam)
class OurTeamAdmin(admin.ModelAdmin):
    list_display = ['name', 'position']


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ['name', 'position']


@admin.register(OurStatus)
class OurStatuslAdmin(admin.ModelAdmin):
    list_display = ['name', 'status']
