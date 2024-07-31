from django.shortcuts import render, redirect, get_object_or_404
from .forms import RegistrationForm, PostForm
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .models import Post


# Create your views here.
@login_required(login_url='/login')
def home(request):
    posts = Post.objects.all()

    # to delete 
    if request.method == "POST":
        post_id = request.POST.get("post-id") # name passed at the frontend
        post = Post.objects.filter(id=post_id).first()
        if post and post.author == request.user:
            post.delete()

    return render(request, "pages/home.html", {'posts':posts})

# write sign-up views 
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            # messages.success("Account Successfully Created")
            return redirect('/home')
    else:
        form = RegistrationForm()
        # messages
    return render(request, 'registration/register.html', {'form':form})

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

def updatePost(request, pk):
    recent_post = get_object_or_404(Post, id=pk)
    # Check if the current user is the owner of the post or has the appropriate permissions
    if recent_post.author != request.user:
        messages.error(request, "You do not have permission to edit this post.")
        return redirect('/home')
    
    form = PostForm(request.POST or None, instance=recent_post)
    if form.is_valid():
        form.save()
        messages.success(request, "Update Successful")
        return redirect('/home')

    return render(request, "pages/update_post.html", {'form': form})

