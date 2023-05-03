from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=3000, null=True, blank=True)
    leftimage = models.ImageField(upload_to='media/',
                                  null=True, blank=True)
    rightimage = models.ImageField(upload_to='media/',
                                   null=True, blank=True)
    additionalright = models.TextField(blank=True, null=True)
    bottomdetails = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

 