from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.

from users.forms import profileUpdateForm, userUpdateForm, RequirementsForm
from users.models import Profile 
from users.models import  Requirements
from django.contrib import messages


@login_required(login_url='login')


def HomePage(request):
    return render (request,'home.html')

def SignupPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1!=pass2:
            return HttpResponse("Your passwords do not match!!")
        else:

            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            profile = Profile.objects.create(user = my_user)
            return redirect('login')
        



    return render (request,'signup.html')

def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse ("Username or Password is incorrect!!!")

    return render (request,'login.html')

def LogoutPage(request):
    logout(request)
    return redirect('login')

# decorator
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Profile

@login_required(login_url='login')
def profile(request):
    if request.method == 'POST':
        new_bio = request.POST.get('bio')
        profile = Profile.objects.get(user=request.user)
        profile.bio = new_bio
        profile.save()
        # messages.success(request, 'Your bio was successfully updated!')
        return redirect('Profile')
    else:
        profile = Profile.objects.get(user=request.user)
        context = {
            'username': request.user.username,
            'email': request.user.email,
            'is_teacher': profile.is_teacher,
            'bio': profile.bio,
        }
        return render(request, 'profile.html', context)


@login_required (login_url='login')
def save_requirements(request):
    if request.method == 'POST':
        form = RequirementsForm(request.POST)
        if form.is_valid():
            # If the form is valid, save the data to the database
            requirements = form.save(commit=False)
            # Populate the user field with the currently logged-in user
            requirements.user = request.user
            # Save the object to the database
            requirements.save()
            # Redirect to the home page or wherever appropriate
            return redirect('home')
    else:
        form = RequirementsForm()
    
    # Render the form template with the form
    return render(request, 'requirements_form.html', {'form': form})

