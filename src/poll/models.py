from django.db import models
from datetime import date


# Create your models here.
class Poll(models.Model):
    name = models.CharField(
        verbose_name='Poll name',
        max_length=80,
    )
    
    start_date = models.DateField(
        verbose_name='Poll start date',
        auto_now=True
    )

    end_date = models.DateField(
        verbose_name='Poll end date',
        default=date(2100, 12, 31)
    )

    description = models.CharField(
        verbose_name='Description',
        blank=True,
        max_length=200
    )


class Question(models.Model):
    poll_id = models.ForeignKey(
        'Poll',
        verbose_name='Poll',
        on_delete=models.CASCADE,
        related_name='questions'
    )
    
    text = models.CharField(
        verbose_name='Question',
        max_length=200,
    )
    
    QUESTION_TYPE = (
        (1, 'Text answer'),
        (2, 'One answer select'),
        (3, 'More than one answer select')
    )

    question_type = models.IntegerField(
        verbose_name='Question type',
        choices=QUESTION_TYPE
    )

    answer = models.CharField(
        verbose_name='Answer',
        max_length=80
    )

class Answer(models.Model):
    user_id = models.IntegerField(
        verbose_name='User ID'
    )

    question = models.ForeignKey(
        'Question',
        on_delete=models.CASCADE,
        verbose_name='Question',
        related_name='answers'
    )

    answer = models.CharField(
        verbose_name='Answer',
        max_length=80
    )


class PollsHistory(models.Model):
    poll = models.ForeignKey(
        'Poll',
        verbose_name='Poll',
        on_delete=models.CASCADE
    )

    user_id = models.IntegerField(
        verbose_name='User iD'
    )