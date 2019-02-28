from django.db import models


class Location(models.Model):
   '''
   Database image model for location data
   '''
   location_name = models.CharField(max_length=50)

class Category(models.Model):
   '''
   Database model for category data
   '''
   category_name = models.CharField(max_length=50)

class Image(models.Model):
   '''
   Database image model for image data
   '''
   image = models.ImageField(upload_to="media/", height_field=None, width_field=None, max_length=None)
   image_name = models.CharField(max_length=50)
   description = models.CharField(max_length=50)
   locale = models.ForeignKey(Location, on_delete=models.CASCADE) 
   category =  models.ForeignKey(Category, on_delete=models.CASCADE)