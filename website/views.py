from django.shortcuts import render ,redirect
from django.contrib.auth import authenticate , login , logout
from django.contrib import messages
from .forms import SignUpForms , Add_record
from .models import Record
# Create your views here.

def home(request):
    records = Record.objects.all()
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
        
    else:
        return render(request,'home.html',{'records' : records})


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

def customer_records(request,pk):
    if request.user.is_authenticated:
        
        customer_record = Record.objects.get(id = pk)
        return render(request, 'records.html', {'customer_record':customer_record})
    else:
        messages.success(request , "You must Be logged ")
        return redirect('home')


def delete_records(request , pk):
    if request.user.is_authenticated:
        delete_it = Record.objects.get(id = pk)
        delete_it.delete()
        messages.success(request,"Records Deleted Successfully")
        return redirect('home')
    else:
        messages.success(request , "You must Be logged ")
        return redirect('home')
    
    
def add_record(request):
    form = Add_record(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                add_record = form.save()
                messages.success(request , "Record Added .....")
                return redirect('home')
        return render(request, 'add_record.html',{'form' : form})
    else:
        messages.success(request , "You must be logged .....")
        return redirect('home')
    
def update_record(request, pk) :
    if request.user.is_authenticated:
        current_record = Record.objects.get(id=pk)
        form = Add_record(request.POST or None, instance=current_record)
        if form.is_valid():
            form.save()
            messages.success(request, "Record Has Been Updated!")
            return redirect('home')
        return render(request, 'update.html', {'form':form})
    else:
        messages.success(request, "You Must Be Logged In...")
        return redirect('home')