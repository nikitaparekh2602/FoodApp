from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import RegisterForm
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'user/register.html',{'form':form})

def logout_view(request):
    logout(request)
    messages.success(request, 'You have been logged out.')
    return render(request, 'user/logout.html')  # Redirect to login or home page after logout

@login_required
def profilepage(request):
    return render(request, 'user/profile.html')
