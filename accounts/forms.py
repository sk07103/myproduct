from datetime import date
from django import forms
from django.contrib.auth.password_validation import validate_password

from .models import User

class RegistUserForm(forms.ModelForm):

    class Meta:
        model = User        
        fields = ['username', 'email', 'date_of_birth', 'picture', 'password']
        labels = {
            'username': 'ユーザー名',
            'email': 'メールアドレス',
            'date_of_birth': '生年月日',
            'picture': '画像',
            'password': 'パスワード',
        }
        widgets = {
            'password': forms.PasswordInput(),
            'date_of_birth': forms.DateInput(attrs={'placeholder':date.today()}),

        }
        requireds = {
            'picture': False
        }

    def save(self, commit=False):
      user = super().save(commit=False)
      validate_password(self.cleaned_data['password'], user)
      user.set_password(self.cleaned_data['password'])
      user.save()
      return user

