from django.shortcuts import render
from django.shortcuts import get_object_or_404, render, redirect
from .models import Header
# Create your views here.

def about(request):
    head = Header.objects.all()
    context = {'head': head}
    return render(request, 'resume/about.html', context)