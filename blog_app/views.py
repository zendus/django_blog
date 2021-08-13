from django.shortcuts import render, get_object_or_404
from blog_app.models import Post, Comment

# Create your views here.
def all_posts(request):
    posts = Post.objects.all().order_by('pk').reverse()[1:]
    lastest_post = Post.objects.latest('created_at')
    context = {
        'posts': posts,
        'latest_post': lastest_post,
        'pk': lastest_post.pk,
    }
    return render(request, 'blog_app/all_posts.html', context)


def read_post(request, pk):
    post = get_object_or_404(Post, pk=pk)

    return render(request, 'blog_app/read_post.html', {'post': post})

def all_articles(request):
    articles = Post.objects.filter(section='article')

    return render(request, 'blog_app/all_articles.html', {'articles': articles})

def all_poems(request):
    poems = Post.objects.filter(section='poem')

    return render(request, 'blog_app/all_poems.html', {'poems': poems})
    

def all_yarns(request):
    yarns = Post.objects.filter(section='yarn')

    return render(request, 'blog_app/all_yarns.html', {'yarns': yarns})

def contact(request):
    
    return render(request, 'blog_app/contact.html')

def login(request):
    pass
