from django.conf import settings
from django.conf.urls.static import static
from django.urls import path,include,url

from . import views

urlpatterns = [
   url('^$', views.home, name="photo_home"),
   url('^search/',views.search, name='photo_search')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)