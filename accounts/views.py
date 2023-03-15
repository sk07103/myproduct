from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import CreateView, DetailView, UpdateView

from .forms import RegistUserForm, LoginUserForm, UpdateUserForm
from .models import User

class RegistUserView(CreateView):

    template_name = 'accounts/regist_user.html'
    form_class = RegistUserForm


class LoginUserView(LoginView):

    template_name = 'accounts/login_user.html'
    authentication_form = LoginUserForm

    def form_valid(self, form):
        remember = form.cleaned_data['remember']
        if remember:
            self.request.session.set_expiry(3600)
        return super().form_valid(form)


class LogoutUserView(LogoutView):

    pass


class DetailUserView(LoginRequiredMixin, DetailView):

    template_name = 'accounts/detail_user.html'
    model = User


class UpdateUserView(LoginRequiredMixin, UpdateView):

    template_name = 'accounts/update_user.html'
    model = User
    form_class = UpdateUserForm

    def get_success_url(self):
        return reverse_lazy('accounts:detail_user', kwargs={'pk':self.kwargs['pk']})


class ChangePasswordView(LoginRequiredMixin, PasswordChangeView):

    template_name = 'accounts/change_password.html'
    success_url = reverse_lazy('accounts:change_password_done')


class ChangePasswordDoneView(LoginRequiredMixin, PasswordChangeDoneView):

    template_name = 'accounts/change_password_done.html'
