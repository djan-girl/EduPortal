from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib import messages
#from django.contrib.auth import login_required


def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']

        if not password1 == password2:
            messages.error(request, f"Passwords do not match")
            return redirect('users:register')

        user = User.objects.create_user(
            username=username,
            password=password1,
            email=email,
            first_name=first_name,
            last_name=last_name)

        user.save()

        return redirect('users:login')
    
    return render(request, 'users/register.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'users/login.html', {'error': 'Invalid username or password'})

    return render(request, 'users/login.html')

@ login_required
def logout_view(request):
    logout(request)
    return redirect('users:login')