from django.shortcuts import render ,redirect
from django.contrib.auth import authenticate , login , logout
from django.contrib import messages

# Create your views here.

def home(request):
    if request.method == "POST":
        username = request.POST['first_name']
        password = request.POST['password']
        
        user = authenticate(request,username = username , password = password )
        
        if user is not None:
            login(request,user)    
            messages.success(request,"Yor Have been logged in")
            return redirect('home')
        else:
            messages.success(request,"There was error logged in , Please Try again ....!")
            return redirect('home')
        
        print(username)
        print(password)
    return render(request,'home.html',{})


def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out....")
    return redirect('home')

def register_user(request):
    return render(request,'register.html',{})
