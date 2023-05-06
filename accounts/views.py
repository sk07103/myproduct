import logging

from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import CreateView, DetailView, UpdateView

from .forms import RegistUserForm, LoginUserForm, UpdateUserForm
from .models import User


logger = logging.getLogger('file')


class RegistUserView(CreateView):

    template_name = 'accounts/regist_user.html'
    form_class = RegistUserForm


class LoginUserView(LoginView):

    template_name = 'accounts/login_user.html'
    authentication_form = LoginUserForm


class LogoutUserView(LogoutView):

    pass


class UpdateUserView(LoginRequiredMixin, UpdateView):

    template_name = 'accounts/update_user.html'
    model = User
    form_class = UpdateUserForm

    def get_success_url(self):
        return reverse_lazy('favoritebeauty:home')

    # 変更するユーザーがログイン中のユーザーであることをチェック
    def get_context_data(self, **kwargs):
        if self.request.user.pk != self.kwargs['pk']:
            raise Http404()
        return super().get_context_data(**kwargs)


class ChangePasswordView(LoginRequiredMixin, PasswordChangeView):

    template_name = 'accounts/change_password.html'
    success_url = reverse_lazy('accounts:change_password_done')


class ChangePasswordDoneView(LoginRequiredMixin, PasswordChangeDoneView):

    template_name = 'accounts/change_password_done.html'
