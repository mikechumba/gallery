from django.db import models


class Location(models.Model):
   '''
   Database image model for location data
   '''
   location_name = models.CharField(max_length=50)

   def __str__(self):
      return self.location_name

class Category(models.Model):
   '''
   Database model for category data
   '''
   category_name = models.CharField(max_length=50)

   def __str__(self):
      return self.category_name
   class Meta:
      verbose_name_plural = "Categories"

class Image(models.Model):
   '''
   Database image model for image data
   '''
   image = models.ImageField(upload_to="media/", height_field=None, width_field=None, max_length=None)
   image_name = models.CharField(max_length=50)
   description = models.CharField(max_length=50)
   locale = models.ForeignKey(Location, on_delete=models.CASCADE) 
   category =  models.ForeignKey(Category, on_delete=models.CASCADE)


   def __str__(self):
      return self.image_name

   def save_image(self):
      self.save()

   def delete_image(self):
      self.delete()

   def update_image(self):
      return self.save()

   @classmethod
   def get_image_by_id(cls,id):
      image = cls.filter_by(pk=id)[:5]
      return image

   @classmethod
   def search_image(cls,cat):
      images = cls.objects.filter(category__unaccent__icontains=cat)
      return images

   @classmethod
   def filter_by_location(cls,location):
      image = Image
      return image
