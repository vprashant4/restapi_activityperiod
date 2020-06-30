from django.shortcuts import render
from .models import User


def home(request):
    getuser = User.objects.all()
    context = {'getuser': getuser}
    return render(request, 'fltapitest/home.html', context)
