from django.db import models

# Create your models here.
class Image(models.Model):
   image = models.ImageField(upload_to="/media", height_field=None, width_field=None, max_length=None)
   image_name = models.CharField(max_length=50)
   description = models.CharField(max_length=50)
   locale = models.ForeignKey(Location, on_delete=models.CASCADE) 
   category =  models.ForeignKey(Category, on_delete=models.CASCADE)

class Location(models.Model):
   location_name = models.CharField(max_length=50)

class Category(models.Model):
   category_name = models.CharField(max_length=50)