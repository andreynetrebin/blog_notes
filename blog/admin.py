from django.contrib import admin
from .models import Post, PostFile, Category
from mptt.admin import MPTTModelAdmin


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish', 'status')
    list_filter = ('status', 'created', 'publish', 'author')
    search_fields = ('title', 'body')
    # prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ('status', 'publish')


@admin.register(PostFile)
class PostFile(admin.ModelAdmin):
    list_display = ('file',)


@admin.register(Category)
class CategoryAdmin(MPTTModelAdmin):
    list_display = ('title', 'parent')
    # prepopulated_fields = {"slug": ("title",)}
