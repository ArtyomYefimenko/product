# -*- coding: utf-8 -*-
__author__ = 'artem'

import unittest

from django.test import Client
from django.core.urlresolvers import reverse_lazy
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
