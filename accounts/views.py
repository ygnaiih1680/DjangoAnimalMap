from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from .models import *

# Create your views here.
def signup(request):
    if request.method == "POST":
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(
        username = request.POST['username'], password=request.POST['password1']
    )

        signup = Signup()
        signup.email = request.POST['email']
        signup.name = request.POST['name']
        signup.user = user
        signup.save()
        auth.login(request, user)
        return redirect('home')
    return render(request, 'signup.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        return render(request, 'login.html', {'error': 'username or password is incorrect.'})
    return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('home')