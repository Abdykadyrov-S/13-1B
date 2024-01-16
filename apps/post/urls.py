from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('contact/', contact, name='contact'),
    path('hi/', hello, name='page-hi'),
    path('goodbye/', goodbye, name='page-bye'),
    path('test/', test, name='page-test'),
]
