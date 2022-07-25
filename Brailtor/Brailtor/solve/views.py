from django.http import HttpResponse , HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

def indexx(request):
    return render(request,'indexx.html')

