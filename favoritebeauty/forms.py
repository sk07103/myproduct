import datetime
import logging
from django import forms

from .models import MyItems, Reviews

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


class ReviewMyitemForm(forms.ModelForm):

    review = forms.ChoiceField(label='今日の調子はどうですか？', choices=Reviews.REVIEW_CHOICES, widget=forms.RadioSelect())

    class Meta:
        model = Reviews
        fields = ['review_date', 'review', 'comment']
        labels = {
            'review_date': '日付',
            'comment': 'コメント'
        }

        requireds = {'comment': False,}
