from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from .models import *
from django.db.models import Q
from django.core.paginator import Paginator
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, reverse
from .forms import CommentForm
from django.core.mail import BadHeaderError, send_mail

# Create your views here.


#for blog page
def blog(request):
    category = Category.objects.all()
    blog = Blog.objects.all()
    categorys = Blog.objects.all().select_related('cat_name')
    blogs = Blog.objects.all().order_by('-blog_timeDate')
    paginator = Paginator(blogs, 10)
    page = request.GET.get('page')
    blogs = paginator.get_page(page)
    context = {
        'category': category,
        'blog': blog,
        'object_list': categorys,
        'blogs': blogs,
    }
    return render(request, 'blog.html', context)

#for readmores
def more(request, slug):
    more = Blog.objects.filter(id=slug).first() 
    category = Category.objects.all()
    blog = Blog.objects.all()
    categorys = Blog.objects.all().select_related('cat_name')
    blogss = get_object_or_404(Blog, id=slug)
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
                   'category': category,
                   'blog': blog,
                   'object_list': categorys,
                   'more':more,
                   })
    
#for search
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

#for contact
def contact(request):
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
        category = Category.objects.all()
        categorys = Blog.objects.all().select_related('cat_name')
        context = {
        'category': category,
        'object_list': categorys,
    }
    return render(request, 'contact.html', context)






