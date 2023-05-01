from django.db import models


class Header(models.Model):
    name = models.CharField(max_length=250)
    intro = models.TextField()
    phone = models.CharField(max_length=30)
    email = models.EmailField(max_length=250)
    address = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class WorkExperience(models.Model):
    title = models.CharField(max_length=250)
    location = models.CharField(max_length=250)
    start = models.CharField(max_length=100)
    end = models.CharField(max_length=100)
    duties = models.TextField()

    def __str__(self):
        return self.title


class Skills(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Education(models.Model):
    name = models.CharField(max_length=250)
    start = models.CharField(max_length=100)
    end = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Certifications(models.Model):
    name = models.CharField(max_length=250)
    start = models.CharField(max_length=100)
    end = models.CharField(max_length=100)

    def __str__(self):
        return self.name