from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import PostForm

# List all posts
def post_list(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'post/index.html', {'posts': posts})

# Create new post
def post_create(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'post/post_form.html', {'form': form, 'title': 'Add Post'})

# Detail view
def post_view(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'post/post_view.html', {'post': post})

# Edit post
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_view', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'post/post_form.html', {'form': form, 'title': 'Edit Post'})

# Delete post
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        post.delete()
        return redirect('post_list')
    return render(request, 'post/confirm_delete.html', {'post': post})
