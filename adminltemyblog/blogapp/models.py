from django.db import models
from django.utils import timezone
from django.utils.safestring import mark_safe
from ckeditor.fields import RichTextField
import sys,os
#from ckeditor_uploader import RichTextUploadingField
# Create your models here.

class Category(models.Model):
    category_title          =  models.CharField(max_length=50, unique=True)
    category_description    =  models.TextField()
    created_date            =  models.DateField()
    updated                 =  models.DateTimeField(default=timezone.now)

    def __str__(self):
        return '%s' % (self.category_title) 

TAGS = (('HOMEPAGE','HOMEPAGE'),('SINGLEPAGE','SINGLEPAGE',),('BLOGPAGE','BLOGPAGE'))
class blog(models.Model):
    cat_id            =  models.ForeignKey(Category, on_delete=models.CASCADE)
    blog_title        =  models.CharField(max_length=50, unique=True)
    blogtype          =  models.TextField(choices=TAGS, max_length=20,default='SINGLEPAGE')
    featured_image    =  models.ImageField(upload_to="uploads", default=True)
    blog_description  =  RichTextField(config_name='portal_config')
    created_date      =  models.DateField()
    is_deleted        = models.BooleanField(default=False)


    def save(self, *args, **kwargs):
        try:
            this = blog.objects.get(id=self.id)
            if this.featured_image != self.featured_image:
                this.featured_image.delete()
        except: pass
        super(blog, self).save(*args, **kwargs)

    def __str__(self):
        return '%s' % (self.blog_title) 
        