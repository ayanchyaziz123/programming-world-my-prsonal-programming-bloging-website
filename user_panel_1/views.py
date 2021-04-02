from django.http.response import HttpResponse
from django.shortcuts import render
from .models import *

# Create your views here.

#index function
def blog(request):
    category = Category.objects.all()
    blog = Blog.objects.all()
    categorys = Blog.objects.all().select_related('cat_name')
    print(categorys)
    context = {
        'category': category,
        'blog': blog,
        'object_list': categorys,
    }
    return render(request, 'blog.html', context)
def more(request, slug):
    more = Blog.objects.filter(id=slug).first() 
    category = Category.objects.all()
    blog = Blog.objects.all()
    categorys = Blog.objects.all().select_related('cat_name')
    print(categorys)
    context = {
        'category': category,
        'blog': blog,
        'object_list': categorys,
        'more':more,
    }
    return render(request, 'more.html', context)


