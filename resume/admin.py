from django.contrib import admin
from .models import Header, WorkExperience, Skill, Education, Certification

# Register your models here.
class Headeradmin(admin.ModelAdmin):
    list_display = ['name', 'intro', 'phone', 'email', 'address']

admin.site.register(Header, Headeradmin)

class SkillAdmin(admin.ModelAdmin):
    list_display = ['name']
admin.site.register(Skill, SkillAdmin)

class WorkExperienceAdmin(admin.ModelAdmin):
    list_display = ['title', 'location', 'start','end']
admin.site.register(WorkExperience, WorkExperienceAdmin)

class EducationAdmin(admin.ModelAdmin):
    list_display = ['title', 'start', 'end']
admin.site.register(Education, EducationAdmin)

class CertificationAdmin(admin.ModelAdmin):
    list_display = ['name', 'start', 'end']
admin.site.register(Certification, CertificationAdmin)