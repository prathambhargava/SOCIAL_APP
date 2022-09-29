from contextlib import redirect_stderr
from django.shortcuts import render, redirect
from django.contrib.auth.models import User,auth
from django.http import HttpResponse
from django.contrib import messages
from matplotlib.pyplot import get
from matplotlib.style import use
from .models import Profile
from django.contrib.auth.decorators import login_required
from django.http import Http404
# Create your views here.

@login_required(login_url='signin')
def index(request):
    user_object = User.objects.get(username=request.user.username)
    user_profile = Profile.objects.get(user=user_object)
    return render(request,'index.html',{'user_profile' : user_profile})

@login_required(login_url='signin')
def setting(request):
        user_profile = Profile.objects.get(user=request.user)
        if request.method == 'POST':
            if request.FILES.get('image') == None:
                image = user_profile.profileimg
                bio = request.POST['bio']
                location = request.POST['location']
                user_profile.profileimg = image
                user_profile.bio = bio
                user_profile.location = location
                user_profile.save()
            if request.FILES.get('image') != None:
                image = request.FILES.get('image')
                bio = request.POST['bio']
                location = request.POST['location']
                user_profile.profileimg = image
                user_profile.bio = bio
                user_profile.location = location
                user_profile.save()

            return redirect('setting')
        return render(request, 'setting.html',{'user_profile' : user_profile})
    
        
    

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2 :
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username taken')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username,password=password)
                user.save()

                user_login = auth.authenticate(username=username, password=password)

                auth.login(request, user_login)
                

                user_model = User.objects.get(username = username)
                new_profile = Profile.objects.create(user=user_model, id_user=user_model.id)
                new_profile.save()
                return redirect('setting')



        else:
            messages.info(request,'Password Not Matching')
            return redirect('signup')




    else:
        return render(request,'signup.html')

def signin(request) :
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'credentials invalid')
            return redirect('signin')
    else:
        return render(request, 'signin.html')

@login_required(login_url='signin')
def logout(request) :

    auth.logout(request)
    return redirect('signin')

@login_required(login_url='signin')
def upload(request):
    return HttpResponse('<h1>upload view</h1>')

