from django.urls import path

from store import views

app_name = "store"
urlpatterns = [
    path('',views.all_products, name="all_products"),
    path('book/<slug:slug>/',views.single_product,name='single_product'),
    path('shop/<slug:category_slug>/',views.category_list,name='category_list'),

]
