import datetime
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.password_validation import validate_password

from .models import User

class RegistUserForm(forms.ModelForm):

    skin_type = forms.ChoiceField(label='ご自身の肌タイプ', choices=User.SKIN_TYPE_CHOICES, widget=forms.RadioSelect())
    date_of_birth = forms.CharField(label='生年月日', max_length=8, min_length=8, help_text='数字8桁で入力（例:1998年1月31日の場合→19950131）')

    class Meta:
        model = User
        fields = ['username', 'email', 'date_of_birth', 'skin_type', 'picture', 'password']
        labels = {
            'username': 'ユーザー名',
            'email': 'メールアドレス',
            'picture': 'プロフィール画像',
            'password': 'パスワード',
            }

        widgets = {
            'password': forms.PasswordInput(),
            }

        requireds = {
            'picture': False,
            }

    def save(self, commit=False):
        user = super().save(commit=False)
        validate_password(self.cleaned_data['password'], user)
        user.set_password(self.cleaned_data['password'])
        user.save()
        return user


class LoginUserForm(AuthenticationForm):

    username = forms.EmailField(label='メールアドレス')
    password = forms.CharField(label='パスワード', widget=forms.PasswordInput())
    remember = forms.BooleanField(label='ログイン状態を保持する', required=False)


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

        widgets = {
            'date_of_birth': forms.DateInput(attrs={'placeholder':datetime.date.today()}),
            }

        requireds = {
            'picture': False,
            }
