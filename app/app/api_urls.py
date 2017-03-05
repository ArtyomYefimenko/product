# -*- coding: utf-8 -*-

from django.conf.urls import url, patterns
from rest_framework.urlpatterns import format_suffix_patterns

from product.api import categories_list, category_detail, product_detail, product_detail_24h


urlpatterns = patterns(
    '',
    url(r'products/$', categories_list, name='products_api'),
    url(r'^products/24h/$', product_detail_24h, name='day_products_api'),
    url(r'^products/(?P<category_slug>\w+)/$', category_detail, name='category_detail_api'),
    url(r'^products/(?P<category_slug>\w+)/(?P<product_slug>\w+)/$', product_detail, name='product_detail_api'),
)


urlpatterns = format_suffix_patterns(urlpatterns)


