from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail
from django.shortcuts import render, redirect, get_object_or_404
from core import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import PostForm
from django.core.paginator import Paginator
from core.constants import STATUS_PUBLISHED
from core.models import *


# Create your views here.
def home(request):
    posts = Post.objects.filter(status=STATUS_PUBLISHED)[:3]
    tags = Tag.objects.all()
    comments = Comment.objects.all()
    return render(request, 'index.html', {'posts': posts, 'tags': tags})


def contact(request):
    contact = ContactInfo.objects.get(status='active')
    return render(request, 'contact.html', {'posts': posts, 'contact': contact})


def post_details(request, slug):
    chosen_post = get_object_or_404(Post, slug=slug)
    comments = Comment.objects.all()
    posts = Post.objects.all()
    tags = Tag.objects.all()
    comments_count = Comment.objects.filter(post=chosen_post).count()
    return render(
        request,
        'post-details.html',
        {
            'posts': posts,
            'chosen': chosen_post,
            'tags': tags,
            'comments': comments,
            'comment_counter': comments_count
        }
    )


def profile(request):
    c_posts = Post.objects.filter(confirmation='confirmed', author=request.user)
    w_posts = Post.objects.filter(confirmation='wait', author=request.user)
    l_posts = Post.objects.filter(like__user=request.user)
    paginator = Paginator(l_posts, 6)
    page = request.GET.get('page')
    items = paginator.get_page(page)
    return render(
        request,
        'profile.html',
        {'c_posts': c_posts,
         'w_posts': w_posts,
         'l_posts': l_posts,
         'items': items
         }
    )


@login_required(login_url='signin')
def send_comment(request):
    comment = request.POST['comment']
    post_id = request.POST['post_id']
    post = Post.objects.get(id=post_id)
    user = request.user
    new_comment = Comment.objects.create(
        content=comment,
        author=user,
        post=post

    )
    return redirect(f'post-details/{post.slug}/')


@login_required(login_url='signin')
def like_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    user = request.user

    # Kullanıcı daha önce bu gönderiyi beğenmişse beğeniyi kaldır
    if user in post.likes.all():
        like = Like.objects.get(user=user, post=post)
        like.delete()
    else:
        Like.objects.create(user=user, post=post)

    return redirect('post_details', slug=post.slug)


@login_required(login_url='signin')
def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.author = request.user
            post = form.save()  # Form verilerini kullanarak yeni bir gönderi oluştur
            return redirect('post_details', slug=post.slug)  # Yeni gönderiye yönlendir
    else:
        form = PostForm()
    return render(request, 'add-post.html', {'form': form})


def support(request):
    subject = request.POST['subject']
    message = request.POST['message']

    Support.objects.create(
        subject=subject,
        user=request.user,
        message=message

    )
    return redirect('contact')


def blog(request):
    post_objs = Post.objects.all()
    tags = Tag.objects.all()
    paginator = Paginator(post_objs, 6)
    page = request.GET.get('page')
    items = paginator.get_page(page)
    return render(request, 'blog.html', {
        'posts': post_objs,
        'tags': tags,
        'items': items
    })


def about(request):
    content = AboutUs.objects.get(status='active')
    return render(request, 'about.html', {
        'posts': posts,
        'content': content
    })


def posts(request):
    return render(request, 'test123.html', {
        'posts': Post.objects.all()
    })


def signup(request):
    if request.method == "POST":
        # username = request.POST.get('username')
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST['pass2']

        if User.objects.filter(username=username):
            messages.error(request, 'Username already exist!')
            return redirect('signin')

        if len(username) > 15:
            messages.error(request, 'Max 10 char at Username!')
            return redirect('signin')

        if not username.isalnum():
            messages.error(request, 'Username must be alpha numeric!')
            return redirect('signin')

        if User.objects.filter(email=email):
            messages.error(request, 'Email already exist!')
            return redirect('signin')

        if len(pass1) < 10:
            messages.error(request, 'Min 10 char at Password!')
            return redirect('signin')

        if pass1 != pass2:
            messages.error(request, 'NOT MATCH PASSWORDS!')
            return redirect('signin')

        myuser = User.objects.create_user(
            username=username,
            email=email,
            password=pass1,
            first_name=fname,
            last_name=lname
        )

        messages.success(request, 'Successfully Created!')

        # Welcome Email

        subject = 'Welcome to Testing World'
        message = f'Hello {myuser.first_name}! Welcome to Testing World'
        from_email = settings.EMAIL_HOST_USER
        to_list = [myuser.email]
        send_mail(subject, message, from_email, to_list, fail_silently=True)

        return redirect('signin')

    return render(request, 'signup.html')


def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST.get('pass1')

        user = authenticate(username=username, password=pass1)

        if user is not None:
            login(request, user)
            messages.success(request, 'Succes LOGIN!!!')
            return redirect('profile')

        else:
            messages.error(request, 'Wrong password or ID')

    return render(request, 'signin.html')


def signout(request):
    logout(request)
    messages.success(request, 'logged out :(')
    return redirect('home')
