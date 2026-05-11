from django.contrib import admin
from .models import Post, Category

# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "content", "is_published", "created_at"]
    search_fields = ["title", "content", "is_published"]
    list_filter = ["is_published", "created_at"]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name"]
    search_fields = ["name"]
    list_filter = ["name"]