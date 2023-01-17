from django.urls import path
from .views import CreateUserView

app_name = 'accounts'

urlpatterns = [
    path('user_create/', CreateUserView.as_view(), name='user_create')
]
