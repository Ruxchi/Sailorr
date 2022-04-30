"""sailorr URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from sailorr import views as sviews
from tryon import views as tviews
# import MainCam

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', sviews.home, name='home'),
    path('about', sviews.about, name='about'),
    path('contact', sviews.contact, name='contact'),
    path('customer', sviews.customer, name='customer'),
    path('portfolio-details', sviews.portfolioDetails, name='portfolio-details'),
    path('portfolio', sviews.portfolio, name='portfolio'),
    path('pricing', sviews.pricing, name='pricing'),
    path('signup', sviews.signup, name='signup'),
    path('login', sviews.login, name='login'),
    path('team', sviews.team, name='team'),
    path('track', sviews.track, name='track'),
    path('tryon', tviews.tryon, name="tryon"),
    # path('tryon', MainCam, name="tryon"),


    
]
