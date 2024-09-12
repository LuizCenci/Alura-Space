from django.urls import path
from users.views import *

urlpatterns = [
    path('login', login, name='login'),
    path('register', register, name='register'),
    path('logout', logout, name='logout')
]