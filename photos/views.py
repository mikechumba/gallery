from django.shortcuts import render

from .models import Image,Category,Location

def home(request):
   images = Image.objects.order_by('-pk')[:10]

   context = {
      'images': images
   }

   return render(request, 'photos/index.html', context)

def search(request):

   if 'search_category' in request.GET and request.GET["search_category"]:
      searched = request.GET.get("search_category")
      category = Category.search_category(searched)
      images = Image.search_image(category.id)

      context = {
         "searched":searched,
         "images": images
      }

      return render(request, 'all-news/search.html', context)

   else:
      msg = "You didn't search for anything"
      return render(request, 'all-news/search.html', {"msg": msg})