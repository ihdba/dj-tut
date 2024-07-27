from django.shortcuts import render, redirect


from django.contrib.auth.decorators import login_required


from .models import Post
from . import forms 

def posts_list(request):
    
    #posts = Post.objects.all()
    # can order the objects in view 
    posts = Post.objects.all().order_by('-date')
    ctx = {
        'posts': posts,
    }
    
    return render(request, 'posts/posts_list.html', ctx) 
    

def post_page(request, slug):

    post = Post.objects.get(slug = slug)
    
    ctx = {'post': post}
    return render(request, 'posts/post_page.html', ctx)


@login_required(login_url="/users/login/")
def new_post_view(request):
    if request.method=="POST":
        form = forms.CreatePostForm(request.POST, request.FILES)
        if form.is_valid():
            newpost = form.save(commit=False)
            newpost.author = request.user
            newpost.save()
            return redirect('posts:list')
    else:
        form = forms.CreatePostForm()
    return render(request, 'posts/new_post.html', { 'form' : form })
    
    