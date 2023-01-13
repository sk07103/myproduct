from django.views.generic import CreateView
from .forms import CreateUserForm

class CreateUserView(CreateView):
    template_name = 'accounts/user_create.html'
    form_class = CreateUserForm

