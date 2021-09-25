from django.contrib.auth import forms
from django.shortcuts import render, redirect
from django.contrib.auth.forms  import UserCreationForm, AuthenticationForm

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if  form.is_valid():
            form.save()
            # login user
            return redirect('articles:list')
    else:
        form = UserCreationForm()
    args = {'form':form}
    return render(request,'accounts/signup.html',args)


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            #login User
            return redirect('articles:list')
    else:
        form = AuthenticationForm()
    args = {'form':form}
    return render(request,'accounts/login.html', args)


# Create your views here.
