from django.db import models
from django.contrib.auth.models import User
from django.utils.html import format_html
from tinymce.models import HTMLField


class Category(models.Model):
    cat_id=models.AutoField(primary_key=True)
    title =models.CharField(max_length=150)
    decription =models.TextField()
    url =models.CharField(max_length=150,)
    image= models.ImageField(upload_to='categortImage')
    date = models.DateTimeField(auto_now_add=True,null=True)

    def image_tag(self):
        return format_html('<img src="/media/{}"  style="width:30px ; height:30px border-radious:50%" />'.format(self.image))
    def __str__(self):
        return str(self.title)

class Post(models.Model):
    post_id =models.AutoField(primary_key=True)
    Content =models.TextField()
    cat = models.ForeignKey(Category,on_delete=models.CASCADE)

    def __str__(self):
        return str(Category.title)
    
class Reader(models.Model):
    reader_id =models.AutoField(primary_key=True)
    name =models.CharField(max_length=150)
    email =models.CharField(max_length=150)
    masssage =models.TextField()
    userdate = models.DateTimeField(auto_now_add=True,null=True)
    
    def __str__(self):
        return str(Reader.name)