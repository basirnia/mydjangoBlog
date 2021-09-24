from django.shortcuts import render
from django.contrib.auth.forms  import UserCreationForm

def signup_view(request):
    form = UserCreationForm()
    args = {'form':form}
    return render(request,'accounts/signup.html', args)

# Create your views here.
