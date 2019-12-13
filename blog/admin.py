from django.contrib import admin
from .models import BlogType,Blog

# Register your models here.

@admin.register(BlogType)
class AdminBlogType(admin.ModelAdmin):
    list_display = ('id','type_name')

@admin.register(Blog)
class AdminBlog(admin.ModelAdmin):
    list_display = ('tittle','blog_type','author','created_time','last_updated_time')