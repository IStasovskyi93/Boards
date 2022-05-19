from django.contrib import admin
from bboard.models import *


class BoardAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'price', 'rubric', 'published')
    list_display_links = ('title', 'content')
    search_fields = ('title', 'content', )


admin.site.register(Board, BoardAdmin)
admin.site.register(Rubric)
