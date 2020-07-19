from django.urls import path


from .views import (AnswersListView, AnswersUpdateView, AnswersDetailView, AnswersDeleteView, AnswersCreateView)
    


urlpatterns = [
    path('<int:pk>/edit/', AnswersUpdateView.as_view(), name='answer_edit'),
    path('<int:pk>/detail/', AnswersDetailView.as_view(), name='answer_detail'),
    path('<int:pk>/delete/', AnswersDeleteView.as_view(), name='answer_delete'),
    path('new/', AnswersCreateView.as_view(), name='answer_new'),
    path('', AnswersListView.as_view(), name='answer_list')
]