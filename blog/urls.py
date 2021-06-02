from django.urls import path
from django.urls.resolvers import URLPattern

from blog.views import AjPost, PostDetailView,blog
urlpatterns = [
    path("",blog, name='blog'),
    path('ajouter_Post/',AjPost, name='ajouter_Post'),
    path("<slug>",PostDetailView.as_view(),name='post')
]