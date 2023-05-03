from django.contrib import admin

from django_summernote.admin import SummernoteModelAdmin
from .models import Project

class ProjectModelAdmin(SummernoteModelAdmin):
    list_display = ('name', 'description', 'otherdetails')
    summernote_fields = ('description', 'otherdetails',)

admin.site.register(Project, ProjectModelAdmin)
