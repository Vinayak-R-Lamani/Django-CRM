from django.shortcuts import render ,redirect
from django.contrib.auth import authenticate , login , logout
from django.contrib import messages
from .forms import SignUpForms
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
        
       
    return render(request,'home.html',{})


def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out....")
    return redirect('home')

def register_user(request):
    if request.method == "POST":
        form = SignUpForms(request.POST)
        if form.is_valid():
            user = form.save()
            
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username = username , password = password)
            login(request , user)
            messages.success(request , 'You have Successfully Register')
            return redirect('home')
        
    else:
        form = SignUpForms()
        
    return render(request, 'register.html', {'form':form})
