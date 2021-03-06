from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.db.models.base import Model
from taggit.managers import TaggableManager

# Create your models here.


class Category(models.Model):
    cat_name = models.CharField(max_length=300)   
    cat_priority = models.IntegerField(blank=True, null=True);
    def __str__(self):
        return self.cat_name

class Blog(models.Model):
    cat_name = models.ForeignKey(Category, on_delete=models.CASCADE)
    blog_author = models.CharField(max_length=200)
    blog_priority = models.IntegerField(blank=True, null=True)
    blog_tags = TaggableManager()
    blog_title = models.CharField(max_length=200)
    blog_descriptions = models.CharField(max_length=600);
    blog_body = RichTextUploadingField(blank=True, null=True)
    blog_views = models.IntegerField(default=0)
    blog_updateDate = models.DateField()
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

class TeamMembers(models.Model):
    tm_priority = models.IntegerField(unique=True)
    tm_name = models.CharField(max_length=80)
    tm_bio = RichTextUploadingField(blank=True, null=True)
    tm_email = models.EmailField()
    tm_github = models.CharField(max_length=100)
    tm_linkedin = models.CharField(max_length=100)
    tm_image = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.tm_name


      