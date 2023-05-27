from django.db import models 

class Customer(models.Model):
    # define the columns of our table in here 
    name = models.CharField(max_length=200)
    industry = models.CharField(max_length=200)