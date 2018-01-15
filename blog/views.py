from django.shortcuts import render, redirect, get_object_or_404
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
from friendship.models import Friend, Follow, FollowingManager
from django.contrib import messages
from django.db.models import Q



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
    posts = Post.objects.all()
    return render(request, 'blog/photogallery.html', {'posts':posts})

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

# Profile picture upload
def upload_pp(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            m = Profile.objects.get(pk=request.user.id)
            m.profilepicture = form.cleaned_data['image']
            m.save()
            return redirect('newUser')
    return HttpResponseForbidden('allowed only via POST')

# Post image upload
def upload_img(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            m = Post.objects.get(pk=Post.id)
            m.img = form.cleaned_data['image']
            m.save()
            return redirect('newUser')
    return HttpResponseForbidden('allowed only via POST')

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()
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

def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    #messages.success(request, "Successfully Deleted")
    return redirect('newUser')



def userlist(request):
    users = User.objects.all()
    return render(request, 'blog/userlist.html', { 'users': users })

def userprofile(request, pk):
    try:
        user = User.objects.get(username=pk)
    except:
        return 404
    posts = Post.objects.filter(author=user.pk)
    if request.user.is_authenticated():
        already_following = FollowingManager.follows(request.user, request.user, user)
        return render(request, 'blog/userprofile.html', { 'posts': posts, 'user': user, 'username': user.username, 'already_following': already_following})
    else:
        return render(request, 'blog/userprofile.html', { 'posts': posts, 'user': user, 'username': user.username,})

#follow and unfollow
def follow(request, pk):
    followed = User.objects.get(username=pk)
    Follow.objects.add_follower(request.user, followed)
    return redirect('userprofile', pk=pk)

def unfollow(request, pk):
    followed = User.objects.get(username=pk)
    Follow.objects.remove_follower(request.user, followed)
    return redirect('userprofile', pk=pk)


#usersearch
def usersearch(request, pk):
    whitespace = False
    for c in pk:
        if c == ' ':
            whitespace = True
    if whitespace == True:
        first, last = pk.split(" ")
        users = User.objects.filter(Q(username__contains=last) | Q(username__contains=first) | Q(first_name_contains=first) | Q(last_name__contains=last))
    else:
        users = User.objects.filter(Q(username__contains=pk) | Q(first_name__contains=pk) | Q(last_name__contains=pk))
    return render(request, 'blog/userlist.html', { 'users': users })

#homefeed
@login_required
def homefeed(request):
    following = Follow.objects.following(request.user)
    posts = Post.objects.filter(author__in=following).order_by('-published_date')
    return render(request, 'blog/feed.html', {'posts': posts})

#download
def download(request, pk):
    post = Post.objects.get(img=pk)
    post.downloads += 1
    return redirect('homefeed')
