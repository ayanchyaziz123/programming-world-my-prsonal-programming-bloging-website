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
    blog_title = models.CharField(max_length=200)
    blog_author = models.CharField(max_length=200)
    blog_body = RichTextUploadingField(blank=True, null=True)
    blog_views = models.IntegerField(default=0)
    blog_thumbnil = models.ImageField(blank=True, null=True)
    blog_timeDate = models.DateTimeField(auto_now_add=True, auto_now=False, blank=True)