from django.db import models


class Location(models.Model):
   '''
   Database image model for location data
   '''
   location_name = models.CharField(max_length=50)

   def __str__(self):
      return self.location_name

   def save_location(self):
      self.save()

   @classmethod
   def get_location(cls,location):
      location = cls.objects.filter(location_name=location)
      return location

class Category(models.Model):
   '''
   Database model for category data
   '''
   category_name = models.CharField(max_length=50)

   def __str__(self):
      return self.category_name

   def save_category(self):
      self.save()

   @classmethod
   def search_category(cls,cat):
      category = cls.objects.filter(category_name__icontains=cat)
      return category
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

   def update_image(self):
      self.delete()

   def delete_image(self):
      image = Image.objects.filter(pk = self.pk)
      image.delete()

   @classmethod
   def get_image_by_id(cls,id):
      image = cls.objects.get(id=id)
      return image

   @classmethod
   def search_image(cls,cat):
      images = cls.objects.filter(category=cat)
      return images

   @classmethod
   def filter_by_location(cls,location):
      image = cls.objects.filter(locale=location)
      return image
