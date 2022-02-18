from django.urls import path
from . import views

urlpatterns=[
    path("",views.login_user, name='login'),
    path('post/',views.submitpost, name='submit'),
    
]