# -*- coding: utf-8 -*-

from datetime import timedelta

from django.db.models import Count
from django.utils import timezone

from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from rest_framework.exceptions import APIException

from .models import Category, Product


@api_view(['GET', ])
def categories_list(request, format=None):
    result = Category.objects.annotate(products_count=Count('category_products')).values(
        'name', 'slug', 'description', 'products_count'
    )
    return Response(result)


@api_view(['GET', ])
def category_detail(request, format=None, **kwargs):
    if not Category.objects.filter(slug=kwargs['category_slug']).exists():
        raise APIException('Category with slug={} not found!'.format(kwargs['category_slug']))
    result = Product.objects.filter(category__slug=kwargs['category_slug']).values('name', 'description', 'price')
    return Response(result)


@api_view(['GET', ])
def product_detail(request, format=None, **kwargs):
    if not Product.objects.filter(slug=kwargs['product_slug'], category__slug=kwargs['category_slug']).exists():
        raise APIException('Product with slug={} and category_slug={} not found!'.format(
            kwargs['product_slug'], kwargs['category_slug']))
    result = Product.objects.filter(category__slug=kwargs['category_slug']).values(
        'name', 'description', 'price').first()
    return Response(result)


@api_view(['GET', ])
@permission_classes((IsAdminUser, ))
def product_detail_24h(request, format=None):
    products = Product.objects.filter(created_at__gte=timezone.now() - timedelta(hours=24)).select_related('category')
    result = [{
        'name': product.name,
        'description': product.description,
        'price': product.price,
        'category_name': product.category.name,
        'category_slug': product.category.slug,
        'date': product.created_at.isoformat()
    } for product in products]
    return Response(result)
