from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
    path('contact/', contact),
    path('hi/', hello),
    path('goodbye/', goodbye),
]
