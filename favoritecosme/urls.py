from django.urls import path
from .views import TestView

app_name = 'favoritecosme'

urlpatterns = [
  path('test/', TestView.as_view(), name='test'),
]
