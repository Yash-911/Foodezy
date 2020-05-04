from pyexpat.errors import messages
import re
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.models import User , auth
from django.core.mail import send_mail
import index.views
# Create your views here.

def login(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']

        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return index.views.newfunc(request)
        else:
            return render(request, 'login3.html')
    else:
        return render(request,'login2.html')


def logout(request):
    auth.logout(request)
    return redirect('/')


def register(request):
    if request.method=='POST':

        first_name=request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']


        password = password1
        flag = 0
        while True:
            if (len(password) < 5):
                flag = -1
                break
            elif not re.search("[a-z]", password):
                flag = -1
                break
            elif not re.search("[A-Z]", password):
                flag = -1
                break
            elif not re.search("[0-9]", password):
                flag = -1
                break
            elif not re.search("[_@$]", password):
                flag = -1
                break
            elif re.search("\s", password):
                flag = -1
                break
            else:
                flag = 0
                print("Valid Password")
                break
        if flag == -1:
            print("Not a Valid Password")
            return render(request, 'register.html')



        if password1==password2:
            if User.objects.filter(username=username).exists():
                print('Username taken')
            elif User.objects.filter(username=username).exists():
                print('Username taken')
            else:
                user = User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
                user.save()
                send_mail('Registration Successful. Thank you for registering with Feastify.',
                 'Dear User,\n\t You are now part of the Feastify Family. We would try our best to please you providing the best services and offers we can.',
                'settings.EMAIL_HOST_USER',
                 [email],
                 fail_silently=False,
                )
                print('user created')
                return redirect('login')
        else:
            print('password not matching..')
        return redirect('/')
    else:
        return render(request,'register.html')