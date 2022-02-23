from turtle import title

from django.contrib.auth.models import User
from django.test import TestCase

from store.models import Category, Product


class TestCategoriesModel(TestCase):
    def setUp(self):
        self.data1 = Category.objects.create(name="django",slug="django")
    
    def test_category_model_entry(self):
        '''
        Test category model data insertion/types/field attributes
        '''
        data = self.data1
        self.assertTrue(isinstance(data, Category))
    
    def test_category_model_entry(self):
        '''
        Test category model default name
        '''
        data = self.data1
        self.assertEqual(str(data),'django')

class TestProductsModel(TestCase):
    def setUp(self):
        Category.objects.create(name="django",slug="django")
        User.objects.create(username="admin")
        self.data1 = Product.objects.create(category_id=1,title='Django For APIS',slug='django-for-apis',created_by_id=1,price='99.00',image="django_for_api")

    def test_product_model_entry(self):
        '''
        Test product model data insertion/types/field attributes
        '''
        data = self.data1
        self.assertTrue(isinstance(data,Product))
    
    def test_product_model_entry(self):
        '''
        Test product model default name
        '''
        data = self.data1
        self.assertTrue(str(data),"Django For APIS")


    
    
        