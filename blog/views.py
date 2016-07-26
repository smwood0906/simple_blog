from django.shortcuts import render
from .models import Post
# Create your views here.\
def home(request):
    p = Post.objects.all()
    print(p)
    context_dict = {'post': p}
    return render(request, 'home.html', context_dict)
