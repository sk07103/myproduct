from django import forms
from .models import User
from django.contrib.auth.password_validation import validate_password

class RegistUserForm(forms.ModelForm):

    class Meta:
        model = User        
        fields = ['username', 'email', 'picture', 'password']
        labels = {
            'username': 'ユーザー名',
            'email': 'メールアドレス',
            'picture': '画像',
            'password': 'パスワード',
        }
        widgets = {
            'password': forms.PasswordInput()
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

