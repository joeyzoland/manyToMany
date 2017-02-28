from django.shortcuts import render, redirect
from models import User, Interest
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, "manyToManyApp/index.html")

def view_users(request):
    context = {
    "users" : User.objects.all()
    }
    return render(request, "manyToManyApp/view_users.html", context)

def view_interests(request):
    userid = request.POST['id']
    context = {
    "name" : User.objects.get(id = userid).name,
    "interests" : User.objects.get(id = userid).interests.all()
    }
    return render(request, "manyToManyApp/view_interests.html", context)

def add(request):
    print "got to the add route"
    username = request.POST["username"]
    interest = request.POST["interest"]
    validation = User.objects.validator(username, interest)
    if validation[0]:
        messages.info(request, "You have successfully logged a name and interest.")
    else:
        for i in validation[1]:
            messages.error(request, validation[2][i])
    return redirect("/")

#Write a function for actually rendering the last page
