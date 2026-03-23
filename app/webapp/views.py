from django.shortcuts import render

from django.http import HttpResponse

def home(request):
    return HttpResponse("Olá Professor! Sou ssua aluna Patricia M em SO! (❁´◡`❁)")
