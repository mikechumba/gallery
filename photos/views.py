from django.shortcuts import render

from .models import Image,Category,Location

def get_locations(location):
   locale = Location.get_location(location) 
   return locale  

def home(request):

   locations = Location.objects.all()

   if 'location' in request.GET and request.GET["location"]:
      selected = request.GET.get("location")
      locale = get_locations(selected)
      if locale:
         images = Image.filter_by_location(locale[0])
      else:
         images = Image.objects.order_by('-pk')[:10]
   else:
      images = Image.objects.order_by('-pk')[:10]

   context = {
      'images': images,
      'locations': locations
   }

   return render(request, 'photos/index.html', context)

def search(request):

   if 'search_category' in request.GET and request.GET["search_category"]:
      searched = request.GET.get("search_category")
      category = Category.search_category(searched)
      if category:
         images = Image.search_image(category[0])
      else:
         images = None

      context = {
         "searched":searched,
         "images": images
      }

      return render(request, 'photos/search.html', context)

   else:
      msg = "You didn't search for anything"
      return render(request, 'all-news/search.html', {"msg": msg})