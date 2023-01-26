from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView

from .forms import RegistUserForm, LoginUserForm

class CreateUserView(CreateView):

    template_name = 'accounts/user_regist.html'
    form_class = RegistUserForm


class LoginUserView(LoginView):

    template_name = 'accounts/user_login.html'
    authentication_form = LoginUserForm

    def form_valid(self, form):
        remember = form.cleaned_data['remember']
        if remember:
            self.request.session.set_expiry(3600)
        return super().form_valid(form)


class UserLogoutView(LogoutView):

    pass
