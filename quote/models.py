from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.conf import settings
from django.utils.translation import gettext_lazy as _

# Create your models here.
# class Customer(models.Model):
#     # user = models.OneToOneField(User, on_delete=models.CASCADE)
#     user = models.OneToOneField(settings.AUTH_USER_MODEL, 
#                                 on_delete=models.CASCADE)
#     # username = models.CharField(max_length=250)
#     # first_name = models.CharField(max_length=250)
#     position = models.CharField(max_length=250)
#     company = models.CharField(max_length=250)
#     address = models.CharField(max_length=300)
#     phone = models.CharField(max_length=30)
#     email = models.EmailField(max_length=250)
#     web_address = models.CharField(max_length=250)

#     def __str__(self):
        # return f'Profile of {self.user.username}'

class Quote(models.Model):
    class Status(models.TextChoices):
        # PENDING = 'PD', _('Pending')
        # REVIEWING = 'RV', _('Reviewing')
        # APPROVED = 'AP', _('Approved')
        PENDING = 'Pending'
        REVIEWING = 'Reviewing'
        APPROVED = 'Approved'
    class Priority(models.TextChoices):
        URGENT  = 'UG', _('Urgent - 1 to week or less')
        NORMAL  = 'NM', _('Normal - 2 to 4 weeks')
        LOW     = 'LW', _('Low - Still Researching')        



    name = models.CharField(max_length=250, null=True,
                            blank=True)
    position = models.CharField(max_length=250, null=True,
                                blank=True)
    company = models.CharField(max_length=250, null=True, 
                               blank=True)
    address = models.CharField(max_length=250, null=True, 
                               blank=True)
    phone = models.CharField(max_length=30, null=True,
                             blank=True)
    email = models.EmailField(max_length=250, null=True,
                             blank=True)
    web_address = models.CharField(max_length=250, null=True,
                                   blank=True)
    
    description = models.TextField()
    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    stat = models.CharField(max_length=20,
                              choices=Status.choices,
                              default=Status.PENDING)
    priority = models.CharField(max_length=2,
                                choices=Priority.choices,
                                default=Priority.NORMAL)
    quoted_price = models.DecimalField(max_digits=250,decimal_places=2,
                                    null=True, blank=True)
    class Meta:
        ordering = ['created']
        indexes = [
            models.Index(fields=['created'])
        ]
    def __str__(self):
        return self.name