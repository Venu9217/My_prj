from django.db import models 

# Create your models here. 
class Farmer_db(models.Model):
    name = models.CharField(max_length=245)
    email = models.CharField(max_length=300,unique=True)
    password = models.CharField(max_length=200)

    


class Crop_db(models.Model):
    farmer= models.ForeignKey(Farmer_db, on_delete=models.CASCADE) 
    
    crop_name = models.CharField(max_length=255)
    land_size = models.FloatField( null=True, blank=True)
    planting_date = models.DateField(null=True, blank=True)
    harvest_date = models.DateField(null=True, blank=True)
    yield_amount = models.FloatField(null=True, blank=True)

    
       
