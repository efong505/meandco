from django.contrib import admin

# Register your models here.
from .models import Quote


# admin.site.register(Quote)
# admin.site.register(Customer)

class QuoteAdmin(admin.ModelAdmin):
    list_display = ['name', 'company', 'phone', 'email','priority']
admin.site.register(Quote, QuoteAdmin)