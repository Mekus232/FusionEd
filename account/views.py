from django.shortcuts import render, HttpResponse

# Create your views here.

def loginUsers(request):
    return render(request, "login.html")