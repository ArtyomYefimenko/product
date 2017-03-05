# -*- coding: utf-8 -*-
__author__ = 'artem'

import json
import unittest

from django.test import Client
from django.core.urlresolvers import reverse, reverse_lazy

from rest_framework import status
from rest_framework.test import APITestCase

from .models import Category, Product


class SimpleTest(unittest.TestCase):

    def setUp(self):
        self.client = Client()

    def test_details(self):
        response = self.client.get(reverse_lazy('products'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['categories']), 0)

        cat_1 = Category.objects.create(
                name='category_1',
                slug='category_slug_1',
                description='description of category 1'
        )
        cat_2 = Category.objects.create(
                name='category_2',
                slug='category_slug_2',
                description='description of category 2'
        )
        response_2 = self.client.get(reverse_lazy('products'))
        self.assertIn(cat_1, response_2.context['categories'])
        self.assertIn(cat_2, response_2.context['categories'])
        self.assertEqual(response_2.context['categories'].count(), 2)


class ApiTest(APITestCase):

    def test_category_detail(self):
        not_exists_url = reverse('category_detail_api', kwargs={'category_slug': 'test'})
        response = self.client.get(not_exists_url)
        self.assertEqual(response.status_code, status.HTTP_500_INTERNAL_SERVER_ERROR)
        cat_1 = Category.objects.create(
                name='category_1',
                slug='category_slug_1',
                description='description of category 1'
        )
        cat_2 = Category.objects.create(
                name='category_2',
                slug='category_slug_2',
                description='description of category 2'
        )
        prod_1 = Product.objects.create(name='prod_1', slug='prod_slug_1', price=1.05, description='', category=cat_1)
        prod_2 = Product.objects.create(name='prod_2', slug='prod_slug_2', price=1.27, description='', category=cat_2)
        prod_3 = Product.objects.create(name='prod_3', slug='prod_slug_3', price=1.18, description='', category=cat_1)

        response_2 = self.client.get(reverse('category_detail_api', kwargs={'category_slug': cat_1.slug}))
        self.assertEqual(response_2.status_code, status.HTTP_200_OK)
        result = [
            {
                "price": prod_3.price,
                "name": prod_3.name,
                "description": prod_3.description
            },
            {
                "price": prod_1.price,
                "name": prod_1.name,
                "description": prod_1.description
            },
        ]
        self.assertEqual(json.loads(response_2.content), result)

        response_3 = self.client.get(reverse('category_detail_api', kwargs={'category_slug': cat_2.slug}))
        self.assertEqual(response_3.status_code, status.HTTP_200_OK)
        result_2 = [
            {
                "price": prod_2.price,
                "name": prod_2.name,
                "description": prod_2.description
            }
        ]
        self.assertEqual(json.loads(response_3.content), result_2)
