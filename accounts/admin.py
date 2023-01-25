from django.contrib import admin
from .models import User

# ファイルアップロードを管理画面で扱えるようにする。
admin.site.register(User)
