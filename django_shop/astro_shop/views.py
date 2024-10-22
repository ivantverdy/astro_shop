from django.shortcuts import render, redirect
from .models import Product
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, LoginForm, UserProfileUpdateForm
from django.contrib.auth.models import User


def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products': products})


def about(request):
    return render(request, 'about.html', {})


def update_user(request):
    if request.user.is_authenticated:
        current_user = User.objects.get(pk=request.user.id)
        form = UserProfileUpdateForm(request.POST or None, instance=current_user)
        if form.is_valid():
            form.save()
            login(request, current_user)
            messages.success(request, 'Your account has been updated!')
            return redirect('home')
        return render(request, 'update_user.html', {'form': form})
    else:
        messages.success(request, 'You are not logged in!')
        return redirect('home')


def login_user(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, 'You are now logged in!')
                return redirect('home')
            else:
                messages.success(request, 'Invalid username or password')
                return redirect('login')
        else:
            messages.success(request, 'There was an error logging in!')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


def logout_user(request):
    logout(request)
    messages.success(request, 'You have logged out successfully')
    return redirect('home')


def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, 'You have registered successfully!')
            return redirect('home')
        else:
            messages.success(request, 'There was an error registering your account!')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


def single_product(request, pk):
    product = Product.objects.get(id=pk)
    return render(request, 'product.html', {'product': product})
