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

    review = forms.ChoiceField(
        label='肌の状態', choices=Reviews.REVIEW_CHOICES, widget=forms.RadioSelect())
    comment = forms.CharField(label='コメント（任意）', widget=forms.Textarea(
        attrs={'rows': 5, 'cols': 60}), required=False)

    class Meta:
        model = Reviews
        fields = ['review', 'comment']
