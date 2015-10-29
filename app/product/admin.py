# -*- coding: utf-8 -*-
__author__ = 'artem'

from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Category, Product
from imperavi.admin import ImperaviAdmin, ImperaviStackedInlineAdmin


class ProductInline(ImperaviStackedInlineAdmin):
    model = Product
    extra = 1


class CategoryAdmin(ImperaviAdmin):
    inlines = [
        ProductInline,
    ]


class ProductAdmin(ImperaviAdmin):
    list_display = [
        'name',
        'category',
        'description',
        'price',
        'created_at',
        'modified_at',
    ]
    search_fields = ('name',)
    ordering = ('name', 'price', 'created_at', 'modified_at',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.unregister(Group)
