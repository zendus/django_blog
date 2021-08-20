from django.contrib import admin
from .models import Post, Comment

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'author', 'section')
    ordering = ('-created_at',)
    search_fields = ['title', 'author__username', 'section']



class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'post', 'opinion')
    search_fields = ['opinion', 'author__username']



admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
