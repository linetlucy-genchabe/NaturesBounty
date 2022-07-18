from django.shortcuts import render,redirect
from django.conf import settings
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.templatetags.static import static
# from django.shortcuts import render, redirect, render_to_response, HttpResponseRedirect
from django.http import HttpResponse, Http404,HttpResponseRedirect
import datetime as dt
from .models import *
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from .forms import *
from .email import send_welcome_email
# Create your views here.




# Create your views here.

def index(request):
    # posts = Posts.objects.all()

    # if request.method == 'POST':
    #     letterform = NewsLetterForm(request.POST)
    #     if letterform.is_valid():
    #         name = letterform.cleaned_data['your_name']
    #         email = letterform.cleaned_data['email']

    #         recipient = NewsLetterRecipients(name = name,email =email)
    #         recipient.save()
    #         send_welcome_email(name,email)

    #         HttpResponseRedirect('index')
    #         #.................
    # else:
    #         letterform = NewsLetterForm()
    
    return render(request, 'index.html')



def contact(request):
    
    
    return render(request, 'contact.html')

def user_login(request):
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']  
        
        user = authenticate (request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,"Welcome , you are now logged in")
            return redirect ("index")
    return render(request, 'registration/login.html')




def register(request):
    
    if request.method =='POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2= request.POST['password2']
        
        if password1 != password2:
            messages.error(request,"confirm your passwords")
            return redirect('/register')
        
        new_user = User.objects.create_user(first_name=first_name,last_name=last_name,username=username,email=email,password=password1)
        
        new_user.save()
        
        return render(request,'registration/login.html')
    return render(request, 'registration/registration.html')

def signout(request):
    logout(request)
    messages.success(request,"You have logged out")
           
    return redirect("/")


@login_required(login_url='/accounts/login/')
def user_profiles(request):
    current_user = request.user
    
    profile = Profile.objects.get(user=request.user)
    # profile = request.user.profile
    
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES,instance=profile)   
        if form.is_valid():
            current_user=current_user
            profile = form.save(commit=False)
            profile.save()
            form.save()
            return redirect('profile')
            
    else:
        form = ProfileUpdateForm()


    return render(request, 'registration/profile.html', {"form":form})

