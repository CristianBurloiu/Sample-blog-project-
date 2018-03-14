from django.shortcuts import render, get_object_or_404
from .models import Post
from .forms import PostForm

# Create your views here.
def post_list(request):
    posts = Post.objects.all()
    return render(request, "blog/post_list.html", {'posts': posts})
    
    
def post_detail(request, id):
    post = get_object_or_404(Post, pk=id)
    return render(request, "blog/post_detail.html", {'post': post})


def create_post(request):
    form = PostForm()
    return render(request, "blog/create_post.html", { 'form': form })