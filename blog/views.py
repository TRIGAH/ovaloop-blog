from django.shortcuts import render,redirect,get_object_or_404
from .models import Post,Photo,Notification,User,Comment
from .forms import CommentForm
from django.contrib import messages

# Create your views here.
def index(request):
    photos = Photo.objects.all()
    return render(request, 'blog/index.html',{"photos":photos})

def contact(request):
    return render(request, 'blog/contact.html')

def blog_index(request):
    photos = Photo.objects.all()
    return render(request, 'blog/blog.html',{"photos":photos})

# def blog_details(request):
#     return render(request, 'blog/blog-details.html')

def blog_details(request, pk):
    post = get_object_or_404(Post, pk=pk)
    photo = Photo.objects.filter(post=post).first()
    comments = Comment.objects.filter(post=post)
    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            Notification.objects.create(
                user=post.author,
                content=f'New comment on your post "{post.title}" by {comment.author}.'
            )
            return redirect('blog_details', pk=pk)
    else:
        comment_form = CommentForm()
    return render(request, 'blog/blog-details.html', {'post': post, 'comments': comments, 'comment_form': comment_form, "photo":photo})



def blog_comment(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your comment has been submitted successfully!')
            return redirect('blog:blog_comment')  # Redirect to a success page or the same page
        else:
            messages.error(request, 'There was an error submitting your comment. Please try again.')
    else:
        form = CommentForm()
    
    return render(request, 'blog/blog-details.html', {'form': form})


def blog_category(request):
    photos = Photo.objects.all()
    return render(request, 'blog/blog-category.html',{'photos': photos})

def blog_list(request):
    photos = Photo.objects.all()
    return render(request, 'blog/blog-list.html',{'photos': photos})



# from django.shortcuts import render, get_object_or_404, redirect
# from django.contrib.auth.decorators import login_required
# from .models import Post, Category, Tag, Comment, Notification
# from .forms import PostForm, CommentForm

# def post_list(request):
#     posts = Post.objects.all()
#     return render(request, 'blog/post_list.html', {'posts': posts})

# def post_detail(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     comments = post.comments.all()
#     if request.method == "POST":
#         comment_form = CommentForm(request.POST)
#         if comment_form.is_valid():
#             comment = comment_form.save(commit=False)
#             comment.post = post
#             comment.author = request.user
#             comment.save()
#             Notification.objects.create(
#                 user=post.author,
#                 content=f'New comment on your post "{post.title}" by {comment.author}.'
#             )
#             return redirect('post_detail', pk=pk)
#     else:
#         comment_form = CommentForm()
#     return render(request, 'blog/post_detail.html', {'post': post, 'comments': comments, 'comment_form': comment_form})

# @login_required
# def post_new(request):
#     if request.method == "POST":
#         form = PostForm(request.POST)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.author = request.user
#             post.save()
#             form.save_m2m()  # Save the many-to-many relationships
#             return redirect('post_detail', pk=post.pk)
#     else:
#         form = PostForm()
#     return render(request, 'blog/post_edit.html', {'form': form})

# @login_required
# def post_edit(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     if request.method == "POST":
#         form = PostForm(request.POST, instance=post)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.author = request.user
#             post.save()
#             form.save_m2m()  # Save the many-to-many relationships
#             return redirect('post_detail', pk=post.pk)
#     else:
#         form = PostForm(instance=post)
#     return render(request, 'blog/post_edit.html', {'form': form})

# @login_required
# def notification_list(request):
#     notifications = Notification.objects.filter(user=request.user, read=False)
#     return render(request, 'blog/notification_list.html', {'notifications': notifications})
