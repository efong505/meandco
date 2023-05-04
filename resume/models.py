from django.db import models


"""
Header section that contains the name, in my example case Edward Fong, 
    the intro to the resume, the title of the position applying for, the phone number, 
    email, website link to another profile project that I created in a previous class, 
    and my address.
"""
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


"""
WORK EXPERIENCE - Class that creates each work experience that contains
    the job title, location of job, start and end date and the duties. 
"""
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


"""
SKILLS - Creates an individual skill that consists of just the name of the skill.
"""
class Skill(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


"""
EDUCATION - Creates an education entry that consists of the title of the degree,
    school the degree was earned at, and the start and end date of the school.
"""
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


"""
CERTIFICATIONS - Creates a certification instance that includes the name, 
    start and end date. 
"""
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