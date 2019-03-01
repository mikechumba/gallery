from django.shortcuts import render

from .models import Image,Category,Location

def home(request):
   images = Image.objects.order_by('-pk')[:5]

   context = {
      'images': images
   }

   return render(request, 'photos/index.html', context)
