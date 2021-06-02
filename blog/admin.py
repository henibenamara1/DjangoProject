from django.contrib import admin
from blog.models import *

admin.site.register(Author)
admin.site.register(Categorie)
admin.site.register(Post)
admin.site.register(Coment)

# Register your models here.
