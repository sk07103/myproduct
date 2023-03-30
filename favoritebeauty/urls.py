from django.urls import path
from .views import TopView, RegistMyitemView

app_name = 'favoritebeauty'

urlpatterns = [
  path('regist_myitem/', RegistMyitemView.as_view(), name='regist_myitem'),
  path('top/', TopView.as_view(), name='top'),
]
