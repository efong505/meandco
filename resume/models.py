from django.db import models


class Header(models.Model):
    name = models.CharField(max_length=250)
    intro = models.TextField()
    title = models.CharField(max_length=250)
    phone = models.CharField(max_length=30)
    email = models.EmailField(max_length=250)
    link = models.CharField(max_length=250)
    address = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class WorkExperience(models.Model):
    title = models.CharField(max_length=250)
    location = models.CharField(max_length=250)
    start = models.DateField()
    end = models.DateField()
    duties = models.TextField()


    class Meta:
        ordering = ['-start', 'end']
        indexes = [
            models.Index(fields=['-start'])
        ]

    def __str__(self):
        return self.title


class Skill(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Education(models.Model):
    title = models.CharField(max_length=250)
    school = models.CharField(max_length=250)
    start = models.DateField()
    end = models.DateField()

    
    class Meta:
        ordering = ['-start', 'end']
        indexes = [
            models.Index(fields=['-start'])
        ]

    def __str__(self):
        return self.title


class Certification(models.Model):
    name = models.CharField(max_length=250)
    start = models.DateField()
    end = models.DateField()


    class Meta:
        ordering = ['-start', 'end']
        indexes = [
            models.Index(fields=['start'])
        ]

    def __str__(self):
        return self.name