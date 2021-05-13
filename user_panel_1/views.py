from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from .models import *
from django.db.models import Q, query
from django.core.paginator import Paginator
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, reverse
from .forms import CommentForm
from django.core.mail import BadHeaderError, send_mail

# Create your views here.


#for blog page
def blog(request):
    categorys = Blog.objects.all().select_related('cat_name')
    categorys = categorys.order_by('cat_name__cat_priority', 'cat_name', 'blog_priority') #sort all data
    blogs = Blog.objects.all().order_by('-blog_date')
    paginator = Paginator(blogs, 10)
    page = request.GET.get('page')
    blogs = paginator.get_page(page)
    recentBlog = Blog.objects.all().order_by('-blog_date')[0:5]
    flag = 0
    context = {
        'object_list': categorys,
        'blogs': blogs,
        'recentBlog': recentBlog,
        'flag': flag,
    }
    return render(request, 'blog.html', context)

#for readmore
def more(request, slug):
    more = Blog.objects.filter(id=slug).first() 
    more.blog_views = more.blog_views + 1
    more.save()
    blogss = get_object_or_404(Blog, id=slug)
    categorys = Blog.objects.all().select_related('cat_name')
    categorys = categorys.order_by('cat_name__cat_priority', 'cat_name', 'blog_priority') #sort all data
    reacentBlog = Blog.objects.all().order_by('-blog_date')[0:5]
    # list of active parent comments
    go_back = slug
    #print("hello world")
    comments = blogss.comments.filter(active=True, parent__isnull=True)
    if request.method == 'POST':
        print("hello me if")
        # comment has been added
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            parent_obj = None
            # get parent comment id from hidden input
            try:
                # id integer e.g. 15
                parent_id = int(request.POST.get('parent_id'))
            except:
                parent_id = None
            # if parent_id has been submitted get parent_obj id
            if parent_id:
                parent_obj = Comment.objects.get(id=parent_id)
                # if parent object exist
                if parent_obj:
                    # create replay comment object
                    replay_comment = comment_form.save(commit=False)
                    # assign parent_obj to replay comment
                    replay_comment.parent = parent_obj
            # normal comment
            # create comment object but do not save to database
            new_comment = comment_form.save(commit=False)
            # assign ship to the comment
            new_comment.blog = blogss
            # save
            new_comment.save()
            return HttpResponseRedirect(reverse('more', args=[str(go_back)]))
    else:
        comment_form = CommentForm()
    return render(request,
                  'more.html',
                  {
                   'comments': comments,
                   'comment_form': comment_form,
                   'blog': blog,
                   'object_list': categorys,
                   'more':more,
                   'recentBlog': reacentBlog,
                   })
    
#for search
def search(request):
    query = request.GET['search']
    search = Blog.objects.filter(Q(blog_title__icontains=query) | Q(blog_body__contains=query))
    total = search.count()
    categorys = Blog.objects.all().select_related('cat_name')
    categorys = categorys.order_by('cat_name__cat_priority', 'cat_name', 'blog_priority') #sort all data
    reacentBlog = Blog.objects.all().order_by('-blog_date')[0:5]
    print(categorys)
    context = {
        'search': search,
        'object_list': categorys,
        'query': query,
        'total': total,
        'recentBlog': reacentBlog,
    }
    return render(request, 'search.html', context)

#for contact
def contact(request):
    reacentBlog = Blog.objects.all().order_by('-blog_date')[0:5]
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        data  = Contact(name=name, email=email, subject=subject, message=message)
        data.save()
        messages.success(request, "Your message was sent successfully.Thanks to you")
        return redirect('blog')
        #print(name, email, subject, message)
    else:    
        categorys = Blog.objects.all().select_related('cat_name')
        categorys = categorys.order_by('cat_name__cat_priority', 'cat_name', 'blog_priority') #sort all data
        context = {
        'object_list': categorys,
        'recentBlog': reacentBlog,
    }
    return render(request, 'contact.html', context)

#date wise search

def date(request, slug):
    reacentBlog = Blog.objects.all().order_by('-blog_date')[0:5]
    categorys = Blog.objects.all().select_related('cat_name')
    categorys = categorys.order_by('cat_name__cat_priority', 'cat_name', 'blog_priority') #sort all data
    date = Blog.objects.filter(blog_date__contains=slug)
    total = date.count()
    query = slug
    context = {
        'date': date,
        'object_list': categorys,
        'recentBlog': reacentBlog,
        'total': total,
        'query': query,
    }
    return render(request, 'date.html', context)

#tags wise search
def tags(request, slug):
    reacentBlog = Blog.objects.all().order_by('-blog_date')[0:5]
    tags = Blog.objects.filter(blog_tags__contains=slug)
    categorys = Blog.objects.all().select_related('cat_name')
    categorys = categorys.order_by('cat_name__cat_priority', 'cat_name', 'blog_priority') #sort all data
    total = tags.count()
    query = slug
    context = {
        'tags': tags,
        'object_list': categorys,
        'recentBlog': reacentBlog,
        'total': total,
        'query': query,
    }
    return render(request, 'tags.html', context)

def author(request, slug):
    reacentBlog = Blog.objects.all().order_by('-blog_date')[0:5]
    author = Blog.objects.filter(blog_author__contains=slug)
    categorys = Blog.objects.all().select_related('cat_name')
    categorys = categorys.order_by('cat_name__cat_priority', 'cat_name', 'blog_priority') #sort all data
    total = author.count()
    query = slug
    context = {
        'author': author,
        'object_list': categorys,
        'recentBlog': reacentBlog,
        'total': total,
        'query': query,
    }
    return render(request, 'author.html', context)    

def about(request):
    reacentBlog = Blog.objects.all().order_by('-blog_date')[0:5]
    categorys = Blog.objects.all().select_related('cat_name')
    categorys = categorys.order_by('cat_name__cat_priority', 'cat_name', 'blog_priority') #sort all data
    print(categorys)
    teamMembers = TeamMembers.objects.all().order_by('tm_priority')

    context = {
        'object_list': categorys,
        'recentBlog': reacentBlog,
        'teamMembers': teamMembers,
    }
    return render(request, 'about.html', context)  
def topBlog(request):
    categorys = Blog.objects.all().select_related('cat_name')
    categorys = categorys.order_by('cat_name__cat_priority', 'cat_name', 'blog_priority') #sort all data
    blogs = Blog.objects.all().order_by('-blog_views')
    paginator = Paginator(blogs, 10)
    page = request.GET.get('page')
    blogs = paginator.get_page(page)
    recentBlog = Blog.objects.all().order_by('-blog_date')[0:5]
    flag = 1
    context = {
        'object_list': categorys,
        'blogs': blogs,
        'recentBlog': recentBlog,
        'flag': flag,
    }
    return render(request, 'blog.html', context) 





