from django.shortcuts import render
from django.http import HttpResponse
from .forms import LoginForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
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

def logout_user(request):
    # Log out the user.
    # since function cannot be same as django method, esle it will turn into recursive calls
    logout(request)
    # Return to homepage.
    return render(request,'users/logout.html')

@login_required
def index(request):
    return render(request,'users/index.html')