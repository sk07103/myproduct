from django.urls import path
from .views import TopView, RegistMyitemView, HomeView

app_name = 'favoritebeauty'

urlpatterns = [
    path('top/', TopView.as_view(), name='top'),
    path('regist_myitem/', RegistMyitemView.as_view(), name='regist_myitem'),
    path('home/', HomeView.as_view(), name='home'),
]
