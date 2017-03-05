from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth.views import logout, login
from django.views.generic import TemplateView

from product.views import CategoryListView, CategoryDetailView, ProductDetailView, Product24ListView
from settings import DEBUG, MEDIA_ROOT


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^imperavi/', include('imperavi.urls')),
    url(r'^$', TemplateView.as_view(template_name='base.html'), name='home'),
    url(r'^products/$', CategoryListView.as_view(), name='products'),
    url(r'^products/24h/$', Product24ListView.as_view(), name='day_products'),
    url(r'^products/(?P<category_slug>\w+)/$', CategoryDetailView.as_view(), name='category_detail'),
    url(r'^products/(?P<category_slug>\w+)/(?P<product_slug>\w+)/$', ProductDetailView.as_view(), name='product_detail'),


    url(r'^accounts/login/$', login, name='login'),
    url(r'^accounts/logout/$', logout, name='logout'),
]


if DEBUG:
    urlpatterns += patterns('',
                            (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
                                'document_root': MEDIA_ROOT}))
