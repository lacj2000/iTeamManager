from django.db import models

class Researcher(models.Model):
    name  = models.CharField(max_length=128)
    email = models.EmailField(max_length=256)
    description = models.CharField(max_length=512)
    img_profile = models.FileField(upload_to='media/images', blank=True)
    
    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=512)
    researchers = models.ManyToManyField(Researcher, related_name='researchers', blank=True)
    img_project = models.FileField(upload_to='media/projects', blank=True)


    def __str__(self):
        return self.name
