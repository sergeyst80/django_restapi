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

    def __str__(self):
        return f'Poll #{self.pk} "{self.name}"'


class Question(models.Model):
    poll = models.ForeignKey(
        Poll,
        verbose_name='Poll',
        on_delete=models.CASCADE,
        related_name='poll_questions'
    )
    
    text = models.CharField(
        verbose_name='Question text',
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

    answer_variants = models.TextField(
        verbose_name='Answer variants',
        max_length=1000,
        blank=True
    )

    correct_answer = models.CharField(
        verbose_name='Correct answer',
        max_length=200
    )

    def __str__(self):
        return f'Question #{self.pk} for poll #{self.poll_id}'


class UserPoll(models.Model):
    poll = models.ForeignKey(
        Poll,
        verbose_name='Poll',
        on_delete=models.CASCADE
    )

    user_id = models.IntegerField(
        verbose_name='User iD'
    )
    

class Answer(models.Model):
    user_poll = models.ForeignKey(
        UserPoll,
        on_delete=models.CASCADE,
        verbose_name='User poll',
        related_name='poll_answers'
    )

    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        verbose_name='Question',
        related_name='question_answers'
    )

    answer = models.CharField(
        verbose_name='Answer',
        max_length=200
    )

    def __str__(self):
        return f'Answer #{self.pk}, question #{self.question} poll #{self.poll}'
