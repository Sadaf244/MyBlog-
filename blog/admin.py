from django.contrib import admin
from .models import Post,Author,Tag,Comment

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields={"slug":("title",)}
    list_filter=("date","tags","author",)
    list_display=("title","author","date",)
    search_fields=("title",)

class CommentAdmin(admin.ModelAdmin):
    list_display=("user_name","post",)

admin.site.register(Post,PostAdmin)
admin.site.register(Author)
admin.site.register(Tag)
admin.site.register(Comment,CommentAdmin)

# Register your models here.
