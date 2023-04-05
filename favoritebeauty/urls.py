from django.urls import path
from .views import TopView, RegistMyitemView, ReviewMyitemView, HomeView

app_name = 'favoritebeauty'

urlpatterns = [
    path('top/', TopView.as_view(), name='top'),
    path('regist_myitem/', RegistMyitemView.as_view(), name='regist_myitem'),
    path('review_myitem/<int:myitem_id>/<str:review_date>',
         ReviewMyitemView.as_view(), name='review_myitem'),
    path('home/', HomeView.as_view(), name='home'),
]
