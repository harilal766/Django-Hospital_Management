from django.urls import path
from . import views

app_name = 'userauth'

urlpatterns = [
    path('profile/',views.profile,name='account_profile'),
]