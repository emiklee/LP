from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'menu_photo', 'price', 'available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name', ]
    fields = ['name', 'category', 'slug', 'image', 'menu_photo', 'description', 'price']
    readonly_fields = ['menu_photo']

    def menu_photo(self, object):
        if object.image:
            return mark_safe(f"<img src='{object.image.url}' width=100>")

    menu_photo.short_description = 'Миниатюра'


admin.site.register(Product, ProductAdmin)
