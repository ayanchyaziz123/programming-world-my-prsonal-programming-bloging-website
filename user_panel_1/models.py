from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.db.models.base import Model

# Create your models here.


class Category(models.Model):
    cat_name = models.CharField(max_length=300)    
    def __str__(self):
        return self.cat_name

class Blog(models.Model):
    cat_name = models.ForeignKey(Category, on_delete=models.CASCADE)
    blog_priority = models.IntegerField(blank=True, null=True)
    blog_tags = models.CharField(max_length=200,  blank=True, null=True)
    blog_title = models.CharField(max_length=200)
    blog_author = models.CharField(max_length=200)
    blog_body = RichTextUploadingField(blank=True, null=True)
    blog_views = models.IntegerField(default=0)
    blog_date = models.DateField(auto_now_add=True, auto_now=False, blank=True)

    def __str__(self):
        return self.blog_title

class Contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.CharField(max_length=500)
    reply = models.BooleanField(default=False)

    def __str__(self):
        return self.email

class Comment(models.Model):
    blog = models.ForeignKey(Blog, related_name='comments', on_delete=models.CASCADE )
    name = models.CharField(max_length=80)
    email = models.EmailField(max_length=200, blank=True)
    body = RichTextUploadingField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    # manually deactivate inappropriate comments from admin site
    active = models.BooleanField(default=True)
    parent = models.ForeignKey('self', null=True, on_delete=models.CASCADE , blank=True, related_name='replies')

    class Meta:
        # sort comments in chronological order by default
        ordering = ('created',)

    def __str__(self):
        return 'Comment by {}'.format(self.name)