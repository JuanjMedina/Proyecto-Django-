from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *
urlpatterns = [
    path('', inicio, name="Home"),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)