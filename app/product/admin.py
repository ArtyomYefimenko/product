# -*- coding: utf-8 -*-
__author__ = 'artem'

from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Category, Product
from imperavi.admin import ImperaviAdmin


class CategoryAdmin(ImperaviAdmin):
    prepopulated_fields = {"slug": ("name", )}
    search_fields = ("name", "slug")
    list_display = search_fields


class ProductAdmin(ImperaviAdmin):
    list_display = [
        'name',
        'category',
        'description',
        'price',
        'created_at',
        'modified_at',
    ]
    search_fields = ('name', 'category__name', 'slug')
    ordering = ('name', 'price', 'created_at', 'modified_at',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.unregister(Group)
