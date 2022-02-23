from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

class Category(models.Model):
    '''
    model of store category
    '''
    name = models.CharField(max_length=300,db_index=True)
    slug = models.SlugField(max_length=300, unique=True)

    class Meta:
        verbose_name = "category"
        verbose_name_plural = "categories"
    
    def get_absolute_url(self):
        return reverse('store:category_list',args=[self.slug])
    
    def __str__(self):
        return self.name

class Product(models.Model):
    '''
    model of store product
    '''
    category = models.ForeignKey(Category,related_name="product",on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="product_creator")
    title = models.CharField(max_length=300)
    author = models.CharField(max_length=300, default='admin')
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to="images/")
    slug = models.SlugField(max_length=300)
    price = models.DecimalField(max_digits=14, decimal_places=2)
    in_stock = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "product"
        verbose_name_plural = "products"
        ordering = ('-created',)
    
    def get_absolute_url(self):
        return reverse('store:product_detail',args=[self.slug])

    def __str__(self):
        return self.title
