
from django.shortcuts import render, redirect
from django.contrib.auth.forms  import UserCreationForm, AuthenticationForm
from django.contrib.auth import login

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if  form.is_valid():
            user = form.save()
            # login user
            login(request,user)
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
            user = form.get_user()
            login(request,user)
            return redirect('articles:list')
    else:
        form = AuthenticationForm()
    args = {'form':form}
    return render(request,'accounts/login.html', args)


# Create your views here.
