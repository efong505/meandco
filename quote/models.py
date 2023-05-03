from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.conf import settings
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _


# User1 = get_user_model()
class Quote(models.Model):
    class Status(models.TextChoices):
        # PENDING = 'PD', _('Pending')
        # REVIEWING = 'RV', _('Reviewing')
        # APPROVED = 'AP', _('Approved')
        NEWSITE = 'New Site'
        EXISTING = 'Existing Site'
        

    class Quoted(models.TextChoices):
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


    name = models.CharField(max_length=250)
    requester = models.ForeignKey(User, 
                                  on_delete=models.CASCADE, related_name='quotes')
    
    position = models.CharField(max_length=250, null=True,
                                blank=True)
    company = models.CharField(max_length=250, null=True, 
                               blank=True)
    address = models.CharField(max_length=250, null=True, 
                               blank=True)
    phone = models.CharField(max_length=30)
    email = models.EmailField(max_length=250)
    web_address = models.CharField(max_length=250, null=True,
                                   blank=True)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    stat = models.CharField(max_length=20,
                              choices=Status.choices,
                              default=Status.NEWSITE)
    quoted = models.CharField(max_length=20,
                              choices=Quoted.choices,
                              default=Quoted.PENDING)
    priority = models.CharField(max_length=2,
                                choices=Priority.choices,
                                default=Priority.NORMAL)
    quoted_price = models.DecimalField(max_digits=250,decimal_places=2,
                                    null=True, blank=True)
    jobfile = models.FileField(upload_to="jobfiles/", null=True, blank=True)


    class Meta:
        ordering = ['created']
        indexes = [
            models.Index(fields=['created'])
        ]

    def __str__(self):
        return self.name
    
class Home(models.Model):
    name = models.CharField("Home", max_length=250)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name