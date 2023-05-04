from django.shortcuts import render
from django.shortcuts import get_object_or_404, render, redirect
from .models import Header, Skill, WorkExperience, Education, Certification


"""
about function - that consists of all of the items of the resume such as
    the header items, skills instances, work experiences, degrees, 
    and certifications.
"""
def about(request):
    head = Header.objects.all()
    skills = Skill.objects.all()
    work = WorkExperience.objects.all()
    education = Education.objects.all()
    certifications = Certification.objects.all()
    context = {'head': head, 'skills':skills, 
                'work':work,'education':education, 
                'certifications': certifications}
    return render(request, 'resume/about.html', context)




