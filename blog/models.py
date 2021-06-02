from django.db import models
from autoslug import AutoSlugField

from django.contrib.auth import get_user_model
from django.db.models.deletion import CASCADE
from django.utils.text import slugify
from django.urls import reverse
User = get_user_model()
class Author(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    profile_image=models.ImageField(upload_to="")
    
    def __str__(self):
        return self.user.username
class Categorie(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "categorie"
        verbose_name_plural="Categories"
class Coment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey('Post',on_delete=models.CASCADE)
    content = models.TextField()
    def __str__(self):
        return self.user.username

class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from='title')
    thumbnail = models.ImageField(upload_to="",null=True,blank=True)
    image_url =models.CharField(max_length=500,default=None,null=True,blank=True)
    overview = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Categorie)

    def __str__(self):
        return self.title
    @property
    def post_link(self):
        return reverse("post", kwargs={
            'slug': self.slug
        })