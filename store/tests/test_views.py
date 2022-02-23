# from unittest import skip
from django.http import HttpRequest
from django.test import TestCase, Client, RequestFactory
from django.urls import reverse
from django.contrib.auth.models import User
from store.models import Category, Product
from store.views import all_products

# @skip("demonstrating skipping")
# class TestSkip(TestCase):
#     def test_skip(self):
#         pass


class TestViewResponse(TestCase):
    def setUp(self):
        self.c = Client()
        self.factory = RequestFactory()
        User.objects.create(username="admin")
        Category.objects.create(name="django", slug="django")
        Product.objects.create(category_id=1, title='Django For APIS', slug='django-for-apis',
                               created_by_id=1, price='5199.00', image="django_for_api")

    def test_url_allowed_hosts(self):
        '''
        testing allowed hosts
        '''
        response = self.c.get('/')
        self.assertEqual(response.status_code, 200)

    def test_homepage(self):
        request = HttpRequest()
        response = all_products(request)
        # html = response.content.decode('utf8')
        # print(html)
        # self.assertIn('<title>Home</title>',html)
        # self.assertTrue(html.startswith('\n<!DOCTYPE html>\n'))
        self.assertEqual(response.status_code,200)

    def test_product_detail_url(self):
        '''
        testing product response url status
        '''
        response = self.c.get(
            reverse('store:product_detail', args=['django-for-apis']))
        self.assertEqual(response.status_code, 200)
    
    def test_category_detail_url(self):
        '''
        testing category response url status
        '''
        response = self.c.get(
            reverse('store:category_list', args=['django']))
        self.assertEqual(response.status_code, 200)

    def test_view_function(self):
        request = self.factory.get('product/django-for-apis')
        response = all_products(request)
        # html = response.content.decode('utf8')
        # print(html)
        # self.assertIn('<title>Home</title>',html)
        # self.assertTrue(html.startswith('\n<!DOCTYPE html>\n'))
        self.assertEqual(response.status_code, 200)
