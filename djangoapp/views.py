from django.shortcuts import render,redirect
from .forms import *
from .forms import RegisterForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# Create your views here.

def home(request):
    return render(request,"home.html")

def package(request):
    return render(request, "package.html")

def about(request):
    return render(request, "about.html")


def contact(request):
    return render(request, "contact.html")

def dubai(request):
    return render(request, "dubai.html")

def paris(request):
    return render(request, "paris.html")

def booking(request):
    return render(request, "booking.html")

def kerala(request):
    return render(request, "kerala.html")

def kashmir(request):
    return render(request, "kashmir.html")

def userreg(request):
  if request.method == 'POST':
    form = RegisterForm(request.POST)
    if form.is_valid():
       form.save()
       return redirect('home')  # Redirect to home page after signup
    else:
        return render(request,'userreg.html', {'form': form})

  else:
    form = RegisterForm()
  return render(request,'userreg.html', {'form': form})
  

def uselog(request):
  if request.method == 'POST':
     form = SigninForm(request, data=request.POST)
     if form.is_valid():
       user = form.get_user()
       login(request, user)
       return redirect('package')  # Redirect to home page after login
  else:
    form =SigninForm()
  return render(request, 'uselog.html', {'form': form})
       
  
def vendor(request):
    if request.method == 'POST':
       nam = request.POST.get('nm')
       psw = request.POST.get('ps')
       ema = request.POST.get('em')
       ven = Vendor(company_name =nam,password=psw,email=ema)
       ven.save()
       return redirect('home')
    else:
        return render (request,"vendor.html")
    
def vendsignin(request):
    if request.method == 'POST':
         form = SigninForm (request.POST)
         if form.is_valid():
             email = Vendor.objects.get('email')
             pswd = Vendor.objects.get('password')
             usr = authenticate(email=email,password=pswd)
             if usr is not None:
                 login(request,usr)
                 return redirect('packreg')
             else:
                 return "invalid email or password"
    else:
        form = SigninForm ()
    return render (request,"vendsignin.html",{'form':form})


def packreg(request):
    if request.method == 'POST':
       amt = request.POST.get('amount')
       packe = request.POST.get('package')
       dys = request.POST.get('days')
       usr = PackReg(amount=amt,package=packe,days=dys)
       usr.save()
       return redirect('home')
    else:
        return render (request,"packagereg.html")
       
    
def usrlogout(request):
    logout(request) 
    return redirect('home')

@login_required
def approvedpack(request):
    st = PackReg.objects.all()
    st = PackReg.objects.filter(approval="True")
    return render(request,"approvedpack.html",{'item':st})


def register(request):
    if request.method == 'POST':
       form = RegisterForm(request.POST)
       if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = RegisterForm()
    return render (request,"register.html",{'form':form})
