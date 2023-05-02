from django.contrib import admin
from .models import Header, WorkExperience, Skills, Education, Certifications

# Register your models here.
class Headeradmin(admin.ModelAdmin):
    list_display = ['name', 'intro', 'phone', 'email', 'address']

admin.site.register(Header, Headeradmin)
