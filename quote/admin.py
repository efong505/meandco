from django.contrib import admin
from .models import Quote, Home

# admin.site.register(Quote)


class QuoteAdmin(admin.ModelAdmin):
    list_display = ['name', 'company', 'phone', 'email','priority']
    
admin.site.register(Quote, QuoteAdmin)


class HomeAdmin(admin.ModelAdmin):
    list_dislapy = ['name', 'updated']

admin.site.register(Home, HomeAdmin)

