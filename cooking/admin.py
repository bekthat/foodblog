from django.contrib import admin
from .models import Category, Posts


class PostsAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'watched','is_published', 'category', 'created_at', 'updated_at']
    list_display_links = ['id', 'title']
    list_editable = ['is_published']

admin.site.register(Category)
admin.site.register(Posts, PostsAdmin)

