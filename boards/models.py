from django.db import models

class Person(models.Model):
	GENDER = (
	    ('M', 'Male'),
	    ('F', 'Female'),
	)
	name = models.CharField(max_length=50)
	gender = models.CharField(max_length=1, choices=GENDER)
	
	def __str__(self):
		return self.name
	

class Organization(models.Model):
	ORGTYPE = (
	    ('BUS', 'Business'),
	    ('NPO', 'Non-profit'),
	    ('GOV', 'Government'),
	)
	name = models.CharField(max_length=100)
	org_type = models.CharField(max_length=3, choices=ORGTYPE)
	members = models.ManyToManyField(Person, through='Relationship')
	
	def __str__(self):
		return self.name
	

class Relationship(models.Model):
	ACTIVE = (
	    ('YES', 'Current'),
	    ('NO', 'Past'),
	)
	POSITION = (
	    ('B', 'Board Member'),
	    ('M', 'Management Team'),
	    ('E', 'Employee'),
	)
	person = models.ForeignKey(Person)
	organization = models.ForeignKey(Organization)
	current = models.CharField(max_length=3, choices=ACTIVE)
	role = models.CharField(max_length=1, choices=POSITION)
	
