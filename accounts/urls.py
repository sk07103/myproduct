from django.urls import path

from .views import RegistUserView, LoginUserView

app_name = 'accounts'

urlpatterns = [
    path('regist_user/', RegistUserView.as_view(), name='regist_user'),
    path('login_user/', LoginUserView.as_view(), name='login_user'),
]
