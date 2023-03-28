from django.shortcuts import render
from django.views.generic.base import TemplateView

class TestView(TemplateView):
    template_name = 'favoritebeauty/test.html'

class TopView(TemplateView):
    template_name = 'favoritebeauty/top.html'
