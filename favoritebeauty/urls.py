from django.urls import path
from .views import TopView, HomeView, RegistMyitemView, ModifyMyitemView, ListTriedMyitemView, ReviewMyitemView, ListReviewView, DetailReviewView

app_name = 'favoritebeauty'

urlpatterns = [
    path('top/', TopView.as_view(), name='top'),
    path('home/', HomeView.as_view(), name='home'),
    path('regist_myitem/', RegistMyitemView.as_view(), name='regist_myitem'),
    path('modify_myitem/<int:pk>', ModifyMyitemView.as_view(), name='modify_myitem'),
    path('list_tried_myitem/', ListTriedMyitemView.as_view(), name='list_tried_myitem'),
    path('review_myitem/<int:myitem_id>/<str:review_date>', ReviewMyitemView.as_view(), name='review_myitem'),
    path('list_review/<int:myitem_id>', ListReviewView.as_view(), name='list_review'),
    path('detail_review/<int:pk>', DetailReviewView.as_view(), name='detail_review'),
]
