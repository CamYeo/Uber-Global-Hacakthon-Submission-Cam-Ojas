
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.db import IntegrityError, models
from django.contrib.auth.models import User
from .models import transportmodel
from django.http import JsonResponse


# Create your views here.

def index(request):
    return render(request, "index.html")

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("home"))
        else:
            return render(request, "login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "login.html")
    
def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()

        except IntegrityError:
            return render(request, "register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "register.html")
    
def home(request):
    user = request.user
    return render(request, "hackathon.html", {
        "users" : User.objects.all(),
    }
    )

def ammend(request):
    user = request.user
    role = request.POST["transportmodelans"]
    x = transportmodel.objects.filter(user = user)
    if x is not None:
        x.delete()
    y = transportmodel.objects.create(user = user, role = role )
    y.save()
    return HttpResponseRedirect(reverse("info"))

def info(request):
     user = request.user
     total_users = User.objects.all().count()
     private_users = transportmodel.objects.filter(role = "Rideshare").count()
     public_users = transportmodel.objects.filter(role = "Public").count()
     private_users = (private_users / total_users) * 100
     public_users = (public_users / total_users) * 100
     return render(request, "hackathon_2.html", {
        "private_users": private_users,
        "public_users": public_users ,
        "total_users": total_users,

    }
    )
