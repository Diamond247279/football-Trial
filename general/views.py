from django.shortcuts import  render, redirect
from django.urls import reverse
from .forms import CustomUserForm
from django.contrib.auth import login,logout
from django.contrib import messages
from .email_backend import EmailBackend
# Create your views here.
def homepage(request):
    context={
        'title':'HOMEPAGE'
    }
    return render(request,'general/index.html',context)

def about(request):
    context={
        'title':'ABOUT US'
    }
    return render(request,'general/about.html',context)


def blog(request):
    context={
        'title':'BLOGS'
    }
    return render(request,'general/blog.html',context)

def services(request):
    context={
        'title':'SERVICES'
    }
    return render(request,'general/services.html',context)

def price(request):
    context={
        'title':'PRICE'
    }
    return render(request,'general/pricing.html',context)

def blogs(request):
    context={
        'title':'BLOG'
    }
    return render(request,'general/blog-single.html',context)

def testimonials(request):
    context={
        'title':'TESTTIMONIALS'
    }
    return render(request,'general/testimonials.html',context)

def portfolio(request):
    context={
        'title':'PORTFOLIO'
    }
    return render(request,'general/portfolio.html',context)

def portfolios(request):
    context={
        'title':'PORTFOLIOS'
    }
    return render(request,'general/portfolio-details.html',context)

def sign_up(request):
    form=CustomUserForm(request.POST or None, request.FILES or None)
    context={
        'title':'SIGN UP',
        'form':form
    }
    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request,'registration successful')
            return redirect(reverse('sign_in'))
        else:
            messages.error(request,'unsuccessful')	
    return render(request, 'general/sign_up.html',context)

def sign_in(request):
    context={
        'title':'SIGN IN'
    }
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=EmailBackend.authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('homepage')
        else:
            messages.error(request, 'invalid credentials')
            return redirect(reverse('sign_in'))
    else:
            return render(request,'general/sign_in.html',context)

def sign_out(request):
    logout(request)
    messages.info(request,'logged out')
    return redirect(reverse('homepage'))

def tactics(request):
    if request.user.is_authenticated:        
        return render(request,'general/tactics.html')
    else:
        messages.error(request, 'you have to login ')
        return redirect(reverse('sign_in'))

