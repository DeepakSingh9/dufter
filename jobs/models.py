from __future__ import unicode_literals

from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User


# Create your models here.
class JobCategory(models.Model):
    name = models.CharField(max_length=128)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(JobCategory, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural="JobCategories"


class Job(models.Model):
    position = models.CharField(max_length=128)
    organisation = models.CharField(max_length=128)
    keyskills = models.CharField(max_length=128)
    location = models.CharField(max_length=128)
    experience = models.CharField(max_length=128)
    summary = models.TextField(max_length=500)
    dateposted = models.DateField(auto_now=True)
    slug = models.SlugField(unique=True)
    jobcategory = models.ForeignKey(JobCategory)


    def __str__(self):
        return self.position


class Profile(models.Model):
    user=models.OneToOneField(User,max_length=128)
    date_of_birth=models.DateField(blank=True,null=True)
    photo=models.ImageField(upload_to='user/%y/%m/%d',blank=True,null=True)
    keyskills=models.CharField(max_length=128,blank=True,null=True)
    experience=models.IntegerField(blank=True,null=True)

    def __str__(self):
        return self.user.username
