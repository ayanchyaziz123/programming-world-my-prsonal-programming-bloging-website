from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog, name='blog'),
    path('more/<str:slug>', views.more, name='more'),
    path('search/', views.search, name='search'),
    path('contact/', views.contact, name='contact'),
]
