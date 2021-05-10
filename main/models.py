from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator
from datetime import timedelta


class Task(models.Model):
    """課題"""
    name = models.CharField('課題名', max_length=50)
    comment = models.TextField('コメント', blank=True, max_length=100)
    stat = models.IntegerField('進捗状況', default=0)
    stat_max = models.IntegerField('最大進捗', default=1, validators=[MinValueValidator(1), MaxValueValidator(1000)])
    deadline = models.DateTimeField('期限日時', default=timezone.now() + timedelta(weeks=1))
    created_at = models.DateTimeField('記録日時', default=timezone.now)

    def __str__(self):
        return self.name
