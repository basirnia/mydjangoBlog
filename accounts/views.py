from django.contrib.auth import forms
from django.shortcuts import render, redirect
from django.contrib.auth.forms  import UserCreationForm

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if  form.is_valid():
            form.save()
            # login
            return redirect('articles:list')
    else:
        form = UserCreationForm()
    args = {'form':form}
    return render(request,'accounts/signup.html',args)

# Create your views here.
