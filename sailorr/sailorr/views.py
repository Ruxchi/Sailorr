from django.shortcuts import render, redirect


def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def customer(request):
    return render(request, 'customer.html')

def portfolioDetails(request):
    return render(request, 'portfolio-details.html')

def portfolio(request):
    return render(request, 'portfolio.html')

def pricing(request):
    return render(request, 'pricing.html')

def signup(request):
    return render(request, 'signup.html')

def login(request):
    return render(request, 'login.html')

def team(request):
    return render(request, 'team.html')

def track(request):
    return render(request, 'track.html')

