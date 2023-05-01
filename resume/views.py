from django.shortcuts import render
from django.shortcuts import get_object_or_404, render, redirect
from .models import Header
# Create your views here.

def about(request):
    about = Header.objects.all()
    context = {'about': about}
    return render(requeset, 'resume/about.html', context)