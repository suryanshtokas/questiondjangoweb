from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.conf import settings
from question.models import Article

# Create your models here.
class Answers(models.Model):
    title = models.CharField(max_length=255, default='Answer')
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    answer = models.TextField()
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article_list')
