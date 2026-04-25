
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .serializers import PostSerializer
from .permissions import IsAuthorOrReadOnly

# Frontend Imports
from django.shortcuts import render
from .models import Post
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required


# Create your views here.
class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

######################################################

# FrontEnd



def home_page(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'home.html', {'posts': posts})


def login_page(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})

    return render(request, 'login.html')



def signup_page(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 != password2:
            return render(request, 'signup.html', {'error': 'Passwords do not match'})

        if User.objects.filter(username=username).exists():
            return render(request, 'signup.html', {'error': 'Username already exists'})

        User.objects.create_user(
            username=username,
            email=email,
            password=password1
        )

        return redirect('login')

    return render(request, 'signup.html')


def create_post_page(request):
    if request.method == "POST":
        Post.objects.create(
            title=request.POST['title'],
            content=request.POST['content'],
            image=request.FILES.get('image'),
            author=request.user
        )
        return redirect('home')

    return render(request, 'create_post.html')


def detail_page(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, 'detail.html', {'post': post})

def logout_page(request):
    logout(request)
    return redirect('home')

@login_required
def edit_post_page(request, id):
    post = get_object_or_404(Post, id=id, author=request.user)

    if request.method == "POST":
        post.title = request.POST['title']
        post.content = request.POST['content']

        if request.FILES.get('image'):
            post.image = request.FILES.get('image')

        post.save()
        return redirect('detail', id=post.id)

    return render(request, 'edit.html', {'post': post})


@login_required
def delete_post_page(request, id):
    post = get_object_or_404(Post, id=id, author=request.user)
    post.delete()
    return redirect('home')
