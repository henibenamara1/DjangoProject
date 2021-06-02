from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic.detail import DetailView
from blog.models import Categorie, Coment, Post
from blog.forms import CommentForm, PostForm
# Create your views here.
def blog(request):
    posts = Post.objects.all()
    categories = Categorie.objects.all()
    context = {
        'categories':categories,
        'posts': posts,
    }
    return render(request,"blog/blog.html",context)

def post(request):
    context = {}
    return render(request,"blog/post.html",context)

class PostDetailView(DetailView):
    model= Post
    template_name = "blog/post.html"
    slug_field = "slug"

    form = CommentForm
    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST)
        if form.is_valid():
            post = self.get_object()
            form.instance.user = request.user
            form.instance.post = post
            form.save()

            return redirect(reverse("post", kwargs={
                'slug': post.slug
            }))
    def get_context_data(self, **kwargs):
        post_comments_count = Coment.objects.all().filter(post=self.object.id).count()
        post_comments = Coment.objects.all().filter(post=self.object.id)
        context=super().get_context_data(**kwargs)
        context.update({
            'form' : self.form,
            'post_comments' : post_comments,
            'post_comments_count': post_comments_count,
        })

        return context

def AjPost(request):
    if request.method == "POST" :
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/blog')
    else :
        form = PostForm() 
    return render(request,'blog\AjPost.html',{'form':form})