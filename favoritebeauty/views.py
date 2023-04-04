import logging

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, FormView
from django.views.generic.base import TemplateView

from .forms import RegistMyitemForm, ReviewMyitemForm
from .models import MyItems, Reviews


logger = logging.getLogger('file')


class TopView(TemplateView):
    template_name = 'favoritebeauty/top.html'


class RegistMyitemView(LoginRequiredMixin, CreateView):

    template_name = 'favoritebeauty/regist_myitem.html'
    form_class = RegistMyitemForm
    success_url = reverse_lazy('favoritebeauty:home')

    # formから受け取ったデータにログインユーザーの情報を加えてDBに保存
    def form_valid(self, form):
        data = form.save(commit=False)
        data.user = self.request.user
        data.save()
        return super().form_valid(form)


class HomeView(LoginRequiredMixin, ListView):

    template_name = 'favoritebeauty/home.html'
    model = MyItems

    def get_context_data(self):
        context = super().get_context_data()
        context['user'] = self.request.user
        return context

    def get_queryset(self, **kwargs):
        queryset = super().get_queryset(**kwargs)
        queryset = queryset.filter(user=self.request.user)
        return queryset


class ReviewMyitemView(LoginRequiredMixin, FormView):

    template_name = 'favoritebeauty/review_myitem.html'
    form_class = ReviewMyitemForm
    success_url = reverse_lazy('favoritebeauty:home')
    model = Reviews

    def form_valid(self, form):
        data = form.cleaned_data
        myitem_id = self.kwargs['pk']
        
        myitem = get_object_or_404(MyItems, pk=myitem_id)
        data['myitem'] = myitem
        obj = Reviews(**data)
        obj.save()

        queryset = Reviews.objects.filter(myitem=myitem_id)
        review_list = []
        for review in queryset:
            review_list.append(review.review)
        logger.info(review_list)

        return super().form_valid(form)

