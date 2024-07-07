from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import BlogPost, Category
from .forms import BlogPostForm

@login_required
def create_blog_post(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            blog_post = form.save(commit=False)
            blog_post.author = request.user
            blog_post.save()
            return redirect('dashboard')
    else:
        form = BlogPostForm()
    return render(request, 'blog/create_blog_post.html', {'form': form})

@login_required
def list_blog_posts(request):
    categories = Category.objects.all()
    blog_posts = BlogPost.objects.filter(draft=False)
    return render(request, 'blog/list_blog_posts.html', {'categories': categories, 'blog_posts': blog_posts})

@login_required
def list_blog_posts_by_category(request, category_name):
    categories = Category.objects.all()
    blog_posts = BlogPost.objects.filter(category=category_name, draft=False)
    return render(request, 'blog/list_blog_posts.html', {'categories': categories, 'blog_posts': blog_posts})


@login_required
def list_user_drafts(request):
    categories = Category.objects.all()
    drafts = BlogPost.objects.filter(author=request.user, draft=True)
    return render(request, 'blog/list_user_drafts.html', {'categories': categories,'drafts': drafts})

@login_required
def list_user_drafts_category(request,category_name):
    categories = Category.objects.all()
    drafts = BlogPost.objects.filter(category=category_name,author=request.user, draft=True)
    return render(request, 'blog/list_user_drafts.html', {'categories': categories,'drafts': drafts})

@login_required
def list_user_published(request):
    categories = Category.objects.all()
    published_posts = BlogPost.objects.filter(author=request.user, draft=False)
    return render(request, 'blog/list_user_published.html', {'categories': categories,'published_posts': published_posts})

@login_required
def list_user_published_category(request,category_name):
    categories = Category.objects.all()
    published_posts = BlogPost.objects.filter(category=category_name,author=request.user, draft=False)
    return render(request, 'blog/list_user_published.html', {'categories': categories,'published_posts': published_posts})
