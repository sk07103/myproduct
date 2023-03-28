from django.urls import path
from .views import TestView, TopView

app_name = 'favoritebeauty'

urlpatterns = [
  path('test/', TestView.as_view(), name='test'),
  path('top/', TopView.as_view(), name='top'),
]
