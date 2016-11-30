from __future__ import unicode_literals
from django.db import models

# Create your models here.

class Advertisement(models.Model):
    title = models.CharField(max_length=200)
    male = models.BooleanField(default=False)
    female = models.BooleanField(default=False)
    age15_20= models.BooleanField(default=False)
    age21_30= models.BooleanField(default=False)
    age31_40= models.BooleanField(default=False)
    age41_50= models.BooleanField(default=False)
    age51= models.BooleanField(default=False)
    qatar_resident= models.BooleanField(default=True)
    source = models.CharField(max_length=200)
    children = models.BooleanField(default=False)
    
    def __unicode__(self):
        return self.title


class User(models.Model):
	username=models.CharField(max_length=200)
	age=models.CharField(max_length=200)
	qatar_resident= models.CharField(max_length=200)
	gender= models.CharField(max_length=200)
	children = models.CharField(max_length=200)

	def __unicode__(self):
		return self.username


class Poster(models.Model):
    title = models.CharField(max_length=200)
    man = models.BooleanField(default=False)
    woman = models.BooleanField(default=False)
    age1520= models.BooleanField(default=False)
    age2130= models.BooleanField(default=False)
    age3140= models.BooleanField(default=False)
    age4150= models.BooleanField(default=False)
    age51= models.BooleanField(default=False)
    qatar_resident= models.BooleanField(default=True)
    source = models.CharField(max_length=200)
    children = models.BooleanField(default=False)

    def __unicode__(self):
        return self.title

class Image(models.Model):
    poster = models.OneToOneField(Poster, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='api/img')
    mimeType = models.CharField(max_length=20)
