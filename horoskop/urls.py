from django.urls import path
from .views import index, ovanH


urlpatterns = [
    path('', index, name='index'),

    path('ovan/', ovanH, name='ovan'),
]
