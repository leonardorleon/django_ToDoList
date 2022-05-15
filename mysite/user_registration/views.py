from django.shortcuts import render, redirect
from .forms import UserRegistrationForm

# Create your views here.

def user_registration(response):
    if response.method == "POST":
        form = UserRegistrationForm(response.POST)
        if form.is_valid():
            form.save()
        
        return redirect("/home")
    else:
        form = UserRegistrationForm()
    
    return render(response, "user_registration/user_registration.html", {"form":form})