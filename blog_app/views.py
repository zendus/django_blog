from django.shortcuts import render, get_object_or_404
from blog_app.models import Post, Comment

# Create your views here.
def all_posts(request):
    posts = Post.objects.all()
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
