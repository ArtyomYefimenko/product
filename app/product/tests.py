# -*- coding: utf-8 -*-
__author__ = 'artem'

import unittest
from django.test import Client

class SimpleTest(unittest.TestCase):
    def setUp(self):
        self.client = Client()

    def test_details(self):

        response = self.client.get('/products/')

        self.assertEqual(response.status_code, 200)

        self.assertNotEqual(response.context['categories'], 0)

if __name__ == '__main__':
    unittest.main()
