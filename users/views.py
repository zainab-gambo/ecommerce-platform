from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import CustomUserCreationForm  

# Signup view
def signup(request):
    if request.method == 'POST':
        form = CustomUser CreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Redirect to a success page
    else:
        form = CustomUser CreationForm()
    return render(request, 'users/signup.html', {'form': form})

# Login view
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to a success page
        else:
            return render(request, 'users/login.html', {'error': 'Invalid credentials'})
    return render(request, 'users/login.html')  # Return the login form on GET request

# Logout view
def logout_view(request):
    logout(request)
    return redirect('home')  # Redirect to a success page

