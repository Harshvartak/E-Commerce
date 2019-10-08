from django.urls import path,include
from .views import *



urlpatterns= [
    path('signup', SignUp, name='signup'),

]
