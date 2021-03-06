from django.core.mail import send_mail
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseForbidden
from blog_app.forms import CommentForm
from blog_app.models import Post
from django.core.paginator import Paginator
from .forms import UserSignupForm
from django.contrib import messages

# Create your views here.
def all_posts(request):
    posts = Post.objects.all().order_by('pk').reverse()[1:]
    paginator = Paginator(posts, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    lastest_post = Post.objects.latest('created_at')
    context = {
        'posts': posts,
        'latest_post': lastest_post,
        'pk': lastest_post.pk,
        'page_obj': page_obj,
    }
    return render(request, 'blog_app/all_posts.html', context)


def read_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comment_form = CommentForm()
    comment_open = False

    if request.user.is_authenticated:
        comment_open = True
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if not request.user.is_anonymous:
            if form.is_valid():
                opinion = form.save(commit=False)
                opinion.author = request.user
                opinion.post = post
                opinion.save()

                return redirect('read_post', pk=post.pk)
        else:
            return HttpResponseForbidden('Forbidden')

    return render(request, 'blog_app/read_post.html', {'post': post, 'comment_open': comment_open, 'comment_form': comment_form})

def all_articles(request):
    articles = Post.objects.filter(section='article').order_by('pk').reverse()
    paginator = Paginator(articles, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'blog_app/all_articles.html', {'articles': articles, 'page_obj': page_obj})

def all_poems(request):
    poems = Post.objects.filter(section='poem').order_by('pk').reverse()
    paginator = Paginator(poems, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'blog_app/all_poems.html', {'poems': poems, 'page_obj': page_obj})
    

def all_yarns(request):
    yarns = Post.objects.filter(section='yarn').order_by('pk').reverse()
    paginator = Paginator(yarns, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'blog_app/all_yarns.html', {'yarns': yarns, 'page_obj': page_obj})


def contact(request):
    if request.method == 'POST':
        person_name = request.POST['person_name']
        person_email = request.POST['person_email']
        person_email_subject = request.POST['subject']
        person_msg = request.POST['person_msg']

        send_mail(
            f'{person_email_subject} - Email From {person_name} with email address {person_email}',# subject
            person_msg,# message
            person_email,# From email
            ['zendusams@gmail.com'],# To email
        )
        
        return render(request, 'blog_app/contact2.html', {'person_name': person_name})

    else:
        return render(request, 'blog_app/contact2.html', {})


def signup(request):
    if request.method == 'POST':
        form = UserSignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Dear {username}, Your account has been created! You are now able to Log in.')
            return redirect('login')
    else:
        form = UserSignupForm()

    return render(request, 'blog_app/signup.html', {'form': form})
