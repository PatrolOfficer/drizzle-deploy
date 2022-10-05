from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse         #to return the user after posting blog

from ckeditor_uploader.fields import RichTextUploadingField  #to post content (interactive and designs)
from taggit.managers import TaggableManager



class Post(models.Model):
    title = models.CharField(max_length=100)
    content = RichTextUploadingField() 
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(default= 'blog_default.jpg', upload_to='blog-pics')
    tags = TaggableManager()


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})