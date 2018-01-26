from __future__ import unicode_literals

from django.db import models
from datetime import datetime
from django import forms

# Create your models here.

class Publisher(models.Model):
    name = models.CharField(max_length = 30)
    address = models.CharField(max_length = 50)
    city = models.CharField(max_length = 60)
    state_province = models.CharField(max_length = 30)
    country = models.CharField(max_length = 50)
    website = models.URLField()
    
    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['name']

class Author(models.Model):
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 40)
    email = models.EmailField(blank = True,verbose_name = 'e-mail')

    def __unicode__(self):
        return u'%s%s'%(self.first_name,self.last_name)

class Book(models.Model):   
    title = models.CharField(max_length = 100)
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher)
    publication_date = models.DateField(blank = True,null = True)
      
    def __unicode__(self):   
        return self.title
   

class Plan(models.Model):
    day = (
			(1,'Monday'),
			(2,'Tuesday'),
			(3,'Wednesday'),
			(4,'Thursday'),
			(5,'Friday'),
			(6,'Saturday'),
			(7,'Sunday'),
 			)
    Not_avaliable_day = models.IntegerField(choices=day,blank = True,null = True)

'''    def __unicode__(self):
        if (self.Not_avaliable_day == 1 ):
            return u'Monday'
        elif (self.Not_avaliable_day == 2 ):
            return u'Tuesday'
'''
    

class Staff(models.Model):
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 40)
    plan = models.ManyToManyField(Plan,verbose_name='Unavailable Time')
    
    

    def __unicode__(self):          # return avaliable name
        return u'%s %s' % (self.first_name, self.last_name)

    def show(self):          # return avaliable name
        return u'%s %s' % (self.first_name, self.last_name)


class Company(models.Model):
    company_name = models.CharField(max_length= 100)
    branch_location = models.CharField(max_length= 100)
    web = models.URLField()
    employee = models.ManyToManyField(Staff)

    def __unicode__(self):          # return avaliable name
        return self.company_name


    

