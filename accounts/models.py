from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.urls import reverse_lazy


class UserManager(BaseUserManager):

    def create_user(self, username, email, password=None):
        if not email:
            raise ValueError('Emailを入力してください')

        user = self.model(email=self.normalize_email(email), username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None):
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):

    username = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField()

    SKIN_TYPE_CHOICES = [
        ('乾燥肌', '乾燥肌'),
        ('普通肌', '普通肌'),
        ('脂性肌', '脂性肌'),
        ('混合肌', '混合肌'),
        ('わからない', 'わからない')
    ]
    skin_type = models.CharField(max_length=5, choices=SKIN_TYPE_CHOICES)

    picture = models.FileField(upload_to='accounts/', default='accounts/default_icon.png', blank=True, null=True)
    regist_date = models.DateField(auto_now=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    # ユーザーのユニークなキーを記述
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    # ユーザ作成が成功した際のリダイレクト先を指定
    def get_absolute_url(self):
        return reverse_lazy('favoritebeauty:top')

    class Meta:
        db_table = 'user'

    def __str__(self):
        return self.username
