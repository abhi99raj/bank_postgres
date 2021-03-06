from django.db import models

# Create your models here.
class Branches(models.Model):
	ifsc = models.TextField(max_length=50)
	bank_name = models.CharField(max_length=200)
	bank_id = models.IntegerField()
	branch = models.CharField(max_length=200)
	address = models.CharField(max_length=500)
	city = models.CharField(max_length=50)
	district = models.CharField(max_length=100)
	state = models.CharField(max_length=50)
	






