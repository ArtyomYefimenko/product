# -*- coding: utf-8 -*-
__author__ = 'artem'

from datetime import timedelta

from django.views.generic import ListView, DetailView
from django.utils import timezone
from django.utils.decorators import method_decorator
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required

from product.models import Category, Product


class CategoryListView(ListView):
    model = Category
    template_name = 'all_categories.html'
    context_object_name = 'categories'


class CategoryDetailView(DetailView):
    model = Category
    template_name = "category_detail.html"
    context_object_name = "category"

    def get_object(self, queryset=None):
        return get_object_or_404(self.model, slug=self.kwargs['category_slug'])


class ProductDetailView(DetailView):
    model = Product
    template_name = "product_detail.html"

    def get_object(self, queryset=None):
        get_object_or_404(Category, slug=self.kwargs['category_slug'])
        return get_object_or_404(self.model, slug=self.kwargs['product_slug'])


class Product24ListView(ListView):
    model = Product
    template_name = 'day_products.html'
    context_object_name = 'prod_24'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(Product24ListView, self).dispatch(request, *args, **kwargs)

    def get_queryset(self):
        return self.model.objects.filter(created_at__gte=timezone.now() - timedelta(hours=24))
