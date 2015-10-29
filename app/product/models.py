# -*- coding: utf-8 -*-
__author__ = 'artem'

from django.db import models
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=85, verbose_name=u'Название категории')
    slug = models.SlugField(max_length=85, unique=True)
    description = models.TextField(max_length=500, verbose_name=u'Описание категории')

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return "/products/%s/" % (self.slug)

    class Meta:
        verbose_name = u'Категория'
        verbose_name_plural = u'Категории'


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='category_products', verbose_name=u'В категории')
    name = models.CharField(max_length=85, verbose_name=u'Название продукта')
    slug = models.SlugField(max_length=85, unique=True)
    description = models.TextField(max_length=500, verbose_name=u'Описание продукта')
    price = models.FloatField(verbose_name=u'Цена продукта')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=u'Добавлен')
    modified_at = models.DateTimeField(auto_now=True, verbose_name=u'Изменен')

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return "/products/%s/%s/" % (self.category.slug, self.slug)

    class Meta:
        ordering = ('-created_at',)
        verbose_name = u'Продукт'
        verbose_name_plural = u'Продукты'
