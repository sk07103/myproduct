import datetime
import logging
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.password_validation import validate_password

from .models import User

logger = logging.getLogger('file')

class RegistUserForm(forms.ModelForm):

    skin_type = forms.ChoiceField(label='ご自身の肌タイプ', choices=User.SKIN_TYPE_CHOICES, widget=forms.RadioSelect())

    class Meta:
        model = User
        fields = ['username', 'email', 'date_of_birth', 'skin_type', 'picture', 'password']
        labels = {
            'username': 'ユーザー名',
            'email': 'メールアドレス',
            'date_of_birth': '生年月日',
            'picture': 'プロフィール画像',
            'password': 'パスワード',
        }

        widgets = {'password': forms.PasswordInput()}
        help_texts = {'date_of_birth': '数字8桁のハイフン(-)区切りで入力してください（例:1998年1月31日の場合→1998-01-31）'}
        requireds = {'picture': False,}

    def save(self, commit=False):
        user = super().save(commit=False)
        validate_password(self.cleaned_data['password'], user)
        user.set_password(self.cleaned_data['password'])
        user.save()
        return user


class LoginUserForm(AuthenticationForm):

    username = forms.EmailField(label='メールアドレス')
    password = forms.CharField(label='パスワード', widget=forms.PasswordInput())


class UpdateUserForm(forms.ModelForm):

    skin_type = forms.ChoiceField(label='ご自身の肌タイプ', choices=User.SKIN_TYPE_CHOICES, widget=forms.RadioSelect())

    class Meta:
        model = User
        fields = ['username', 'email', 'date_of_birth', 'skin_type', 'picture']
        labels = {
            'username': 'ユーザー名',
            'email': 'メールアドレス',
            'date_of_birth': '生年月日',
            'picture': 'プロフィール画像',
        }

        help_texts = {'date_of_birth': '数字8桁のハイフン(-)区切りで入力してください（例:1998年1月31日の場合→1998-01-31）'}
        requireds = {'picture': False,}

    # 設定されているプロフィール画像をクリアした場合はデフォルトの画像を自動で設定する
    def save(self, commit=False):
        user = super().save(commit=False)
        if self.cleaned_data['picture'] is False:
            user.picture = 'accounts/default_icon.png'
        user.save()
        return user

