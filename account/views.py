from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
# from django.contrib.auth import update_session_auth_hash


def register_page(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")

        newUser = User(username=username, email=email)
        newUser.set_password(password)
        newUser.save()

        login(request, newUser)
        messages.success(request,"You have successfully registered...")

        return redirect("home")

    context = {
        "form": form,
    }

    return render(request, 'register.html', context)


def login_page(request):
    form = LoginForm(request.POST or None)

    context = {
        "form": form,
    }

    if form.is_valid():
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            user = None

        if user is not None:
            user = authenticate(username=user.username, password=password)
        
        if user is None:
            context['error'] = "Invalid credentials"
            return render(request, "login.html", context)
       
        login(request, user)
        
        messages.success(request,"You have successfully registered...")

        return redirect("home")

    return render(request, 'login.html', context)


def logout_page(request):
    logout(request)
    return redirect("home")



def delete_account(request):
    if request.method=="POST":
        user=request.user
        user.delete()
        messages.success(request,"Your account has been successfully deleted...")
        return redirect("home")
    
    else:
        messages.error(request,"You have made an invalid request...")
        return redirect('profile')
    

#########################################################

