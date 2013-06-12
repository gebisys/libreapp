from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_at'
    fields = ('title', 'content', 'published', 'author')
    list_display = ('title', 'created_at', 'author')
    list_filter = ('created_at', 'author__username')
    search_fields = ['title', 'author__username']
    
    class Media:
        js = (
            'https://dl.dropboxusercontent.com/u/60582062/site/js/tinymce/tinymce.min.js',
            'https://dl.dropboxusercontent.com/u/60582062/site/js/tinymce/textarea.js',
        )
admin.site.register(Post, PostAdmin)