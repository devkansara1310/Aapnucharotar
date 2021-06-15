from django.contrib.auth import login, logout, authenticate
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import redirect, render
from django.contrib import messages
from django.views.generic import CreateView
from .forms import CustomerSignUpForm, BloggerSignUpForm, listerSignUpForm, vendorSignUpForm
from .models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
from blogproject.settings import EMAIL_HOST_USER
from django.template import Context
from django.core.mail import send_mail
from .models import User, customer
from . import forms
from django.contrib.auth.hashers import check_password


def register(request):
    return render(request, 'signup.html')


def customer_register(request):
    if request.method == 'POST':
        form = CustomerSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            #logic for sending email
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            htmly = get_template('email.html')
            d = {'username': username}
            subject, from_email, to = 'welcome', 'your_email@gmail.com', email
            html_content = htmly.render(d)
            msg = EmailMultiAlternatives(subject, html_content, from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            msg.send()
            messages.success(request, 'Your account has been created ! You are now able to log in')
            return redirect('login')
    else:
        form = CustomerSignUpForm()
    return render(request, 'customer_register.html', {'form': form, 'title': 'reqister here'})

def blogger_register(request):
    if request.method == 'POST':
        form = BloggerSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            #logic for sending email
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            htmly = get_template('email.html')
            d = {'username': username}
            subject, from_email, to = 'welcome', 'your_email@gmail.com', email
            html_content = htmly.render(d)
            msg = EmailMultiAlternatives(subject, html_content, from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            msg.send()
            messages.success(request, f'Your account has been created ! You are now able to log in')
            return redirect('login')
    else:
        form = BloggerSignUpForm()
    return render(request, 'blogger_register.html', {'form': form, 'title': 'reqister here'})

def lister_register(request):
    if request.method == 'POST':
        form = listerSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            #logic for sending email
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            htmly = get_template('email.html')
            d = {'username': username}
            subject, from_email, to = 'welcome', 'your_email@gmail.com', email
            html_content = htmly.render(d)
            msg = EmailMultiAlternatives(subject, html_content, from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            msg.send()
            messages.success(request, f'Your account has been created ! You are now able to log in')
            return redirect('login')
    else:
        form = listerSignUpForm()
    return render(request, 'lister_register.html', {'form': form, 'title': 'reqister here'})

def vendor_register(request):
    if request.method == 'POST':
        form = vendorSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            #logic for sending email
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            htmly = get_template('email.html')
            d = {'username': username}
            subject, from_email, to = 'welcome', 'your_email@gmail.com', email
            html_content = htmly.render(d)
            msg = EmailMultiAlternatives(subject, html_content, from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            msg.send()
            messages.success(request, f'Your account has been created ! You are now able to log in')
            return redirect('login')
    else:
        form = vendorSignUpForm()
    return render(request, 'vendor_register.html', {'form': form, 'title': 'reqister here'})


def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None :
                login(request,user)
                return redirect('/')
            else:
                messages.error(request,"Invalid username or password")
        else:
                messages.error(request,"Invalid username or password")
    return render(request, 'registration/login.html',
    context={'form':AuthenticationForm()})


def logout_view(request):
    logout(request)
    return redirect('/')
