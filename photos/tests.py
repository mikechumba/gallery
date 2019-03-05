from django.test import TestCase

from .models import Image,Location,Category


def create_location_instance():
   new_location = Location(location_name='Nairobi')
   return new_location

def create_image_instance(location,cat):
   new_image = Image(image = 'default.jpg',image_name = 'Default Picture',description = 'Some picture',locale_id = location.id, category_id = cat.id)
   return new_image

def create_category_instance():
   new_category = Category(category_name = "Travel")
   return new_category

class LocationTest(TestCase):

   def setUp(self):
      self.new_location = create_location_instance()
      
   def test_location_instance(self):
      self.assertTrue(isinstance(self.new_location,Location))

   def test_save_location(self):
      self.new_location.save_location()
      locations = Location.objects.all()
      self.assertTrue(len(locations),1)


class CategoryTest(TestCase):

   def setUp(self):
      self.new_category = create_category_instance()
      
   def test_category_instance(self):
      self.assertTrue(isinstance(self.new_category,Category))

   def test_save_category(self):
      self.new_category.save_category()
      categories = Category.objects.all()
      self.assertTrue(len(categories),1)

class ImageTest(TestCase):

   def setUp(self):
      self.location = create_location_instance()
      self.category = create_category_instance()
      self.location.save_location()
      self.category.save_category()
      self.new_image = create_image_instance(self.location,self.category)

   def test_instance(self):
      self.assertTrue(isinstance(self.new_image,Image))


   def test_save_image(self):   
      self.new_image.save_image()
      images = Image.objects.all()
      self.assertTrue(len(images),1)

   def test_get_image_by_id(self):
      self.new_image.save_image()
      pk = self.new_image.pk
      image = Image.get_image_by_id(pk)
      self.assertEqual(image,self.new_image)

   def test_search_image_by_category(self):
      self.new_image.save_image()
      images = Image.search_image(self.category)[:1]
      self.assertTrue(self.new_image in images)

   def test_filter_by_category(self):
      self.new_image.save_image()
      images = Image.filter_by_location(self.location)[:1]
      self.assertTrue(self.new_image in images)

   def test_delete_image(self):
      self.new_image.delete_image()
      images = Image.objects.all()
      self.assertTrue(len(images)<1)
