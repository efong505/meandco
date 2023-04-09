from django.contrib import admin
from .models import Quote

# admin.site.register(Quote)


class QuoteAdmin(admin.ModelAdmin):
    list_display = ['name', 'company', 'phone', 'email','priority']
admin.site.register(Quote, QuoteAdmin)