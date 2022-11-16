from django.contrib import admin
from retreat.models import *

# @admin.register(Retreat)
class RetreatAdmin(admin.ModelAdmin):
    list_display = ['title', 'date_added']
    fieldsets = (
        (None, {
            "fields": (
                'title','body','img'
            ),
        }),
        ('Perks', {
            "fields": (
                'included','excluded'
            ),
        }),
        (None, {
            "fields": (
                'know_before_you_go',
            ),
        }),
        ('Days', {
            "fields": (
                'day_1',
                'day_2',
                'day_3',
                'day_4',
                'day_5',
                'day_6',
                'day_7',
                'day_8',
                'day_9',
                'day_10',
            ),
        }),
    )
    
    class Media:
        # css = {
        #     'all': ('css/admin/style.css',)
        # }
        js = ('js/tinymcecustom.js',)

admin.site.register(Retreat,RetreatAdmin)