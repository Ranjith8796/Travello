from django.shortcuts import render
from .models import destination

def indexx(request):
    
    dests= destination.objects.all()

    return render(request,'travello/index.html',{'dests':dests})
