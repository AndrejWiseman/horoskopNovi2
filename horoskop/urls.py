from django.urls import path
from .views import index, horoskop_view


urlpatterns = [
    path('', index, name='index'),
    path('horoskop/<str:znak>/', horoskop_view, name='horoskop'),
]
