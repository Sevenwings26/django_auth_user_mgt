from django.shortcuts import render, redirect
from .forms import RegistrationForm, PostForm
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .models import Post

# Create your views here.
@login_required(login_url='/login')
def home(request):
    posts = Post.objects.all()
    if request.method == "POST":
        post_id = request.POST.get("post-id")
        post = Post.objects.filter(id=post_id).first()
        if post and post.author == request.user:
            post.delete()
        # print(post_id)
    return render(request, "pages/home.html", {'posts':posts})


@login_required(login_url='/login')
def createPost(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('/home')
    else:
        form = PostForm()
    return render(request, "pages/create_post.html", {"form":form})
    

# write sign-up views 
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success("Account Successfully Created")
            return redirect('/home')
    else:
        form = RegistrationForm()
    return render(request, 'registration/register.html', {"form": form})
