from django.urls import path, include
from .views import fir, ind
urlpatterns = [
  path('index/', fir),
  path('pizza/', ind)
]