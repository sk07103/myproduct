import datetime
import logging
from django import forms

from .models import MyItems

logger = logging.getLogger('file')

class RegistMyitemForm(forms.ModelForm):

    class Meta:
        model = MyItems
        fields = ['category', 'brand', 'name', 'price']
        labels = {
            'category': 'カテゴリー',
            'brand': 'ブランド',
            'name': 'アイテム名',
            'price': '価格',
        }


