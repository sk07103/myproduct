from django.urls import path

from .views import CreateUserView, LoginUserView

app_name = 'accounts'

urlpatterns = [
    path('user_create/', CreateUserView.as_view(), name='user_create'),
    path('user_login/', LoginUserView.as_view(), name='user_login'),
]
