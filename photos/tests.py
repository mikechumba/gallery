from django.test import TestCase

from .models import Image,Location,Category


def create_location_instance():
   new_location = Location(location_name='Nairobi')
   return new_location

def create_image_instance():
   

class ImageTest(TestCase):

   def setUp(self):
      self.image = Image(image = 'default.jpg',image_name = 'Default Picture',description = 'Some picture',locale = 'Nairobi', category = 'Misc')

   def test_instance(self):
      self.assertTrue(isinstance(self.image,Image))