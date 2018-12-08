from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User

# Create your views here.
def login(request):
    return render(request, 'users/login.html')

def register(request):
    return render(request, 'users/register.html')

def checkout(request, total, id):
    pass

def process_login(request):
    if User.objects.validate(request.POST):
        user = User.objects.get(email=request.POST['email'])
        request.session['user_id'] = user.id
    else:
        error = 'Email or password is incorrect, please verify or register.'
        messages.error(request, error)
        return redirect('/login')
    return redirect('/store/index')

def process_register(request):
    errors = User.objects.register_validate(request.POST)

    if errors:
        for error in errors:
            messages.error(request, error)
    else:
        user =User.objects.create_user(request.POST)
        request.session['user_id'] = user.id
        return redirect('/store/index')

    return redirect('/register')
