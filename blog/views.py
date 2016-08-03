from django.shortcuts import render
from .models import Post
# Create your views here.\
def home(request):
    p = Post.objects.all().order_by('-id')
    print(p)
    context_dict = {'post': p}
    return render(request, 'home.html', context_dict)

def blog(request, slug, cat):
    post = Post.objects.get(slug=slug)
    context_dict = {'post': post}
    return render(request, 'post.html', context_dict)

def cat(request, cat):
    post = Post.objects.filter(category__slug=cat)
    context_dict = {'post': post}
    return render(request, 'category.html', context_dict)