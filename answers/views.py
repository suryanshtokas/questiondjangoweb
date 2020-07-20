from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .models import Answers

# Create your views here.
class AnswersListView(LoginRequiredMixin, ListView):
    model = Answers
    template_name = 'article_list.html'
    login_url = 'login'
    context_object_name = 'all_answers_list'

class AnswersDetailView(LoginRequiredMixin, DetailView):
    model = Answers
    template_name = 'answers_detail.html'
    login_url = 'login'

class AnswersUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Answers
    fields = ('title', 'answer')
    template_name = 'answers_edit.html'
    success_url = reverse_lazy('answer_list')
    login_url = 'login'
    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class AnswersDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Answers
    template_name = 'answers_delete.html'
    success_url = reverse_lazy('answer_list')
    login_url = 'login'
    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class AnswersCreateView(LoginRequiredMixin, CreateView):
    model = Answers
    template_name = 'answers_new.html'
    fields = ('title', 'answer', 'article')
    login_url = 'login'
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


