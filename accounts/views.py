from django.views.generic import CreateView
from .forms import RegistUserForm

class CreateUserView(CreateView):
    template_name = 'accounts/user_regist.html'
    form_class = RegistUserForm

