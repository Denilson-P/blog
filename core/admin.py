from django.contrib import admin

from .models import User, Post, Image, Category, Comment, Like


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("user", "email")


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "content", "publication_date", "author")


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ("post", "image", "description")


@admin.register(Category)
class CategoryAmdin(admin.ModelAdmin):
    list_display = ("name", "description", "created_at")


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("user", "post", "content", "created_at")


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ("user", "post", "created_at")
