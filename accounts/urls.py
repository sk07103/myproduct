from django.urls import path

from .views import RegistUserView, LoginUserView, LogoutUserView, DetailUserView, UpdateUserView, ChangePasswordView, ChangePasswordDoneView

app_name = 'accounts'

urlpatterns = [
    path('regist_user/', RegistUserView.as_view(), name='regist_user'),
    path('login_user/', LoginUserView.as_view(), name='login_user'),
    path('logout_user/', LogoutUserView.as_view(), name='logout_user'),
    path('detail_user/<int:pk>', DetailUserView.as_view(), name='detail_user'),
    path('update_user/<int:pk>', UpdateUserView.as_view(), name='update_user'),
    path('change_password/', ChangePasswordView.as_view(), name='change_password'),
    path('change_password_done/', ChangePasswordDoneView.as_view(), name='change_password_done'),
]
