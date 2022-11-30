from django.urls import path
from .views import home,palki

urlpatterns = [
    path('', home),
    path('palki/', palki),
]