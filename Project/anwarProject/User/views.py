from django.shortcuts import render
from .forms import loginForm,post_form
from User.models import user,post
from django.contrib import messages
# Create your views here.


def login_user(request):
    fm=loginForm(request.POST)
    pf=post_form(request.POST)
    if request.method=="POST":
        email1=request.POST.get("email")
        password1=request.POST.get("password")
        df=user.objects.filter(email=email1,password=password1)
        if len(df)==0:
             fm=loginForm(request.POST)
        else:
            df2=user.objects.get(email=email1,password=password1)
            return render(request,'post.html',{'form':pf,'user':df2})
    return render(request,'index.html',{'form':fm})


def pst_form(request):
    pf=post_form()
    return render(request,'post.html',{'form':pf})
