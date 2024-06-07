from django.shortcuts import render
from django.http import HttpResponse
from .forms import LoginForm
from django.contrib.auth import authenticate,login
# Create your views here.

def user_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request,username=data['username'],password=data['password'])
            if user is not  None:
                login(request,user)
                return HttpResponse("User Authenticated and Logged IN")
            else:
                return HttpResponse("Invalid Login")
    else:
        form = LoginForm()
    return render(request,'users/login.html',{'form':form})
