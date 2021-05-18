from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog, name='blog'),
    path('topBlog/', views.topBlog, name='topBlog'),
    #path('<slug:blo>/', views.more, name='more'),
    path('/<str:slug>', views.mores, name='more'),
    path('date/<str:slug>', views.date, name='date'),
    path('tags/<str:slug>', views.tags, name='tags'),
    path('author/<str:slug>', views.author, name='author'),
    path('search/', views.search, name='search'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]
