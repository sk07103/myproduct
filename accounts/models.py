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
    picture = models.FileField(upload_to='accounts/', blank=True, null=True)
    regist_date = models.DateField(auto_now=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    # ユーザーのユニークなキーを記述
    USERNAME_FIELD = 'email'    
    REQUIRED_FIELDS = ['username']

    # ユーザ作成が成功した際のリダイレクト先を指定
    def get_absolute_url(self):
        return reverse_lazy('favoritecosme:top')

    class Meta:
        db_table = 'user'

    def __str__(self):
        return self.username
