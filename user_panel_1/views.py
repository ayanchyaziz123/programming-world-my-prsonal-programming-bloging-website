from django.http.response import HttpResponse
from django.shortcuts import render
from .models import *
from django.db.models import Q
from django.core.paginator import Paginator

# Create your views here.

#index function
def blog(request):
    category = Category.objects.all()
    blog = Blog.objects.all()
    categorys = Blog.objects.all().select_related('cat_name')
    blogs = Blog.objects.all()
    paginator = Paginator(blogs, 3)
    page = request.GET.get('page')
    blogs = paginator.get_page(page)
    context = {
        'category': category,
        'blog': blog,
        'object_list': categorys,
        'blogs': blogs,
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

def search(request):
    query = request.GET['search']
    blog = Blog.objects.filter(Q(blog_title__icontains=query) | Q(blog_body__contains=query))
    total = blog.count()
    category = Category.objects.all()
    categorys = Blog.objects.all().select_related('cat_name')
    print(categorys)
    context = {
        'category': category,
        'blog': blog,
        'object_list': categorys,
        'query': query,
        'total': total,
    }
    return render(request, 'search.html', context)




