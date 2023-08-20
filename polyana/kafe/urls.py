from django.urls import path, re_path
from .views import *
from django.views.decorators.cache import cache_page

urlpatterns = [
    path('', cache_page(60)(KafeHome.as_view()), name='home'),
    path('menu/', cache_page(60)(KafeMenu.as_view()), name='menu'),
    path('about/', cache_page(60)(Kafe_About.as_view()), name='about'),
    path('delivery/', cache_page(60) (Kafe_Delivery.as_view()), name='delivery'),
    path('contact/', cache_page(60)(KafeContact.as_view()), name='contact'),
    path('category/<slug:category_slug>/', cache_page(60)(KafeCategory.as_view()), name='category'),
    path('products/<slug:products_slug>/', cache_page(60)(KafePost.as_view()), name='products')

]
