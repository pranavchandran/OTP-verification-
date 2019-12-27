from django.shortcuts import render,redirect
from .forms import loginform
from django.contrib import messages
from twilio.rest import Client
import random
from django.core.mail import EmailMessage
from django.contrib.auth.forms import User
from django.contrib.auth.decorators import login_required

from django.core.exceptions import ValidationError

# Create your views here.

def index(request):
    return render(request,'home/index.html')

def signup(request):
    form = loginform(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            mobile = form.cleaned_data.get('Phone')
            username = form.cleaned_data.get('username')
            email1 = form.cleaned_data.get('Email')
            otp = random.randint(0000,9999)
            request.session['OTP_1']=otp
            account = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx' #your account of twilio
            token = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx' #token of twilio
            client = Client(account, token)
            client.messages.create(from_='+16415696832', to="" + str(mobile),body='Welcome ' + str(username) + ' to our Aliensworld verifcation code is ' + str(otp))
            email = EmailMessage('Account activation',str(otp),to=[email1])
            email.send()
            return redirect('home:otp')
    return render(request,'home/signup.html',{'form':form})


def otp(request):
    if request.method == 'POST':
        otp1 = request.session['OTP_1']
        otp = request.POST.get('otp')
        if int(otp1)==int(otp):
            messages.success(request, "Welcome to AliensWorld")
            return render(request,'home/index.html')
        else:
            messages.info(request, 'sorry you typed wrong OTP')
    return render(request,'home/otpverification.html')


