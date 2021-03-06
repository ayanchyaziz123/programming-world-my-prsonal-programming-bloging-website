from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog, name='blog'),
    path('topBlog/', views.topBlog, name='topBlog'),
    #path('<slug:blo>/', views.more, name='more'),
    path('morees/<str:more_slug>/<str:more_slug2>', views.mores, name='more_page'),
    path('date/<str:slug>', views.date, name='date'),
    path('tags/<slug:tag_slug>', views.tags, name='tags'),
    path('author/<str:slug>', views.author, name='author'),
    path('search/', views.search, name='search'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]
