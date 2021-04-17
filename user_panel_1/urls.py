from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog, name='blog'),
    #path('<slug:blo>/', views.more, name='more'),
    path('more/<str:slug>', views.more, name='more'),
    path('date/<str:slug>', views.date, name='date'),
    path('tags/<str:slug>', views.tags, name='tags'),
    path('search/', views.search, name='search'),
    path('contact/', views.contact, name='contact'),
]
