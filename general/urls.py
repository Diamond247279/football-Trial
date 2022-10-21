from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('',homepage,name='homepage'),
    path('about',about,name='about'),
    path('blogs',blogs,name='blogs'),
    path('blog',blog,name='blog'),
    path('services',services,name='services'),
    path('price',price,name='price'),
    path('portfolio',portfolio,name='portfolio'),
    path('portfolios',portfolios,name='portfolios'),
    path('testimonials',testimonials,name='testimonials'),
    path('sign_up',sign_up,name='sign_up'),
    path('sign_in',sign_in,name='sign_in'),
    path('sign_out',sign_out,name='sign_out'),
    path('tactics',tactics,name='tactics'),
    
]
