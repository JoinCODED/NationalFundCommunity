from django.shortcuts import render


def home (request):
    return render(request,"home.html")
def article1 (request):
    return render(request,"article1.html")
def article2 (request):
    return render(request,"article2.html")
def article3 (request):
    return render(request,"article3.html")
