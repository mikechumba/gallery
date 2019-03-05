from django.test import TestCase

from .models import Image,Location,Category


def create_location_instance():
   new_location = Location(location_name='Nairobi')
   return new_location

def create_image_instance(location,cat):
   new_image = Image(image = 'default.jpg',image_name = 'Default Picture',description = 'Some picture',locale = location, category = cat)
   return new_image

def create_category_instance():
   new_category = Category(category_name = "Travel")
   return new_category

class ImageTest(TestCase):

   def setUp(self):
      location = create_location_instance()
      category = create_category_instance()
      self.new_image = create_image_instance(location,category)

   def test_instance(self):
      self.assertTrue(isinstance(self.image,Image))