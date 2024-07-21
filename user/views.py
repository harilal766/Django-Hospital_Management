from django.shortcuts import render

# Create your views here.
def signup(request):
    return(render,'signup.html')


def signout(request):
    return(render,'signout.html')