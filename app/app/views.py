# -*- coding: utf-8 -*-
__author__ = 'artem'

from django.views.generic import ListView, DetailView
from product.models import Category, Product
from django.utils import timezone
from datetime import datetime, timedelta
from django.db.models import F


class CategoryListView(ListView):
    model = Category
    template_name = 'all_categories.html'
    context_object_name = 'categories'


class CategoryDetailView(ListView):
    model = Product
    template_name = "category_detail.html"

    def get_queryset(self):
        return self.model.objects.filter(category__slug=self.kwargs['category_slug'])

    def get_context_data(self, **kwargs):
        context = super(CategoryDetailView, self).get_context_data(**kwargs)
        context['category'] = Category.objects.get(slug=self.kwargs['category_slug'])
        return context


class ProductDetailView(DetailView):
    model = Product
    template_name = "product_detail.html"

    def get_object(self, queryset=None):
        return self.model.objects.get(slug=self.kwargs['product_slug'])


class Product24ListView(ListView):
    model = Product
    template_name = 'day_products.html'
    context_object_name = 'prod_24'

    def get_queryset(self):
        return self.model.objects.filter(created_at__gte=timezone.now() - timedelta(hours=24))