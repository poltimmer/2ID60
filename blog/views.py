from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Post, Profile
from django.contrib.auth import login, authenticate
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from blog.forms import SignUpForm, ImageUploadForm
from django.http.response import HttpResponseForbidden, HttpResponse
from django.contrib.auth.models import User
from .forms import PostForm
from django.contrib.auth.decorators import login_required



def index(request):
    """
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})
    """
    return render(request, 'blog/index.html')

def examples(request):
    return render(request, 'blog/examples.html', {})

@login_required
def newUser(request):
    posts = Post.objects.filter(author=request.user)
    user = request.user
    return render(request, 'blog/newUser.html', {'posts':posts})

def discover(request):
    return render(request, 'blog/discover.html', {})

def photogallery(request):
    return render(request, 'blog/photogallery.html', {})

def jobgallery(request):
    return render(request, 'blog/jobgallery.html', {})




def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('newUser')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})




def simple_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'blog/simple_upload.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'blog/simple_upload.html')

def upload2(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            m = Profile.objects.get(pk=request.user.id)
            m.profilepicture = form.cleaned_data['image']
            m.save()
            return HttpResponse('image upload success, go back to continue')
    return HttpResponseForbidden('allowed only via POST')

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('newUser')
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})
