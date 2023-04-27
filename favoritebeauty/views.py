import logging

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, FormView, UpdateView, DetailView
from django.views.generic.base import TemplateView

from .forms import RegistMyitemForm, ModifyMyitemForm, ReviewMyitemForm
from .models import MyItems, Reviews


logger = logging.getLogger('file')


class TopView(TemplateView):
    template_name = 'favoritebeauty/top.html'


class HomeView(LoginRequiredMixin, ListView):

    template_name = 'favoritebeauty/home.html'
    model = MyItems

    def get_context_data(self):
        context = super().get_context_data()
        context['user'] = self.request.user
        return context

    def get_queryset(self, **kwargs):
        queryset = super().get_queryset(**kwargs)
        queryset = queryset.filter(user=self.request.user, tried=False)
        return queryset


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


class ModifyMyitemView(LoginRequiredMixin, UpdateView):

    template_name = 'favoritebeauty/modify_myitem.html'
    form_class = ModifyMyitemForm
    model = MyItems
    success_url = reverse_lazy('favoritebeauty:home')

    # myitemの所有者とログイン中のユーザーが一致しているかをチェック
    def get_context_data(self, **kwargs):
        myitem_obj = get_object_or_404(MyItems, pk=self.kwargs['pk'])
        if myitem_obj.user.id != self.request.user.pk:
            raise Http404()
        return super().get_context_data(**kwargs)


class ReviewMyitemView(LoginRequiredMixin, FormView):

    template_name = 'favoritebeauty/review_myitem.html'
    form_class = ReviewMyitemForm
    success_url = reverse_lazy('favoritebeauty:home')
    model = Reviews

    def get_context_data(self, **kwargs):

        # myitemの所有者とログイン中のユーザーが一致しているかをチェック
        myitem_obj = get_object_or_404(MyItems, pk=self.kwargs['myitem_id'])
        if myitem_obj.user.id != self.request.user.pk:
            raise Http404()
        
        # テンプレートにmyitemとreview_dateを渡す
        context = super().get_context_data()
        context['myitem'] = myitem_obj
        review_date = self.kwargs['review_date']
        context['review_date'] = review_date.replace("-", "/")
        return context

    def form_valid(self, form):
        data = form.cleaned_data
        myitem_id = self.kwargs['myitem_id']
        review_date = self.kwargs['review_date']

        # レビュー対象アイテムのオブジェクトを取得し、レビューのオブジェクトに紐付けて保存
        myitem_obj = get_object_or_404(MyItems, pk=myitem_id)
        data['myitem'] = myitem_obj
        data['review_date'] = review_date
        review_obj = Reviews(**data)
        review_obj.save()

        # 今回レビューを登録したアイテムに対するレビューを全件取得
        queryset = Reviews.objects.filter(myitem=myitem_id)

        # 取得したレビューの平均値を算出し、アイテムのratingの値を更新し保存
        review_list = []
        for review in queryset:
            review_list.append(review.review)
        review_ave = sum(review_list) / len(review_list)
        myitem_obj.rating = review_ave
        myitem_obj.save()

        return super().form_valid(form)


class ListTriedMyitemView(LoginRequiredMixin, ListView):

    template_name = 'favoritebeauty/list_tried_myitem.html'
    model = MyItems

    def get_context_data(self):
        context = super().get_context_data()
        context['user'] = self.request.user
        return context

    def get_queryset(self, **kwargs):
        queryset = super().get_queryset(**kwargs)
        queryset = queryset.filter(user=self.request.user, tried=True)
        return queryset


class ListReviewView(LoginRequiredMixin, ListView):

    template_name = 'favoritebeauty/list_review.html'
    model = Reviews

    def get_context_data(self, **kwargs):

        # myitemの所有者とログイン中のユーザーが一致しているかをチェック
        myitem_obj = get_object_or_404(MyItems, pk=self.kwargs['myitem_id'])
        if myitem_obj.user.id != self.request.user.pk:
            raise Http404()

        # テンプレートにmyitemを渡す
        context = super().get_context_data()
        context['myitem'] = myitem_obj
        return context


    def get_queryset(self, **kwargs):
        queryset = super().get_queryset(**kwargs)
        myitem = self.kwargs['myitem_id']
        queryset = queryset.filter(myitem=myitem)
        return queryset


class DetailReviewView(LoginRequiredMixin, UpdateView):
    template_name = 'favoritebeauty/detail_review.html'
    form_class = ReviewMyitemForm
    model = Reviews

    def get_success_url(self):
        review = get_object_or_404(Reviews, pk=self.kwargs['pk'])
        return reverse_lazy('favoritebeauty:list_review', kwargs={'myitem_id': review.myitem_id})

    def get_context_data(self, **kwargs):

        # myitemの所有者とログイン中のユーザーが一致しているかをチェック
        review_obj = get_object_or_404(Reviews, pk=self.kwargs['pk'])
        myitem_obj = get_object_or_404(MyItems, pk=review_obj.myitem.id)
        if myitem_obj.user.id != self.request.user.pk:
            raise Http404()
        
        # テンプレートにreviewを渡す
        context = super().get_context_data(**kwargs)
        context['review'] = get_object_or_404(Reviews, pk=self.kwargs['pk'])
        return context
