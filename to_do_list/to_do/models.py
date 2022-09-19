from django.db import models


class Task(models.Model):
    task_text = models.TextField(verbose_name='Текст задачи', max_length=3000, null=False, blank=False)
    state = models.CharField(verbose_name='Состояние', max_length=300, null=False, blank=False, default='new')
    deadline = models.DateTimeField(verbose_name='Дедлайн')

    def __str__(self):
        return f'{self.task_text} {self.state} {self.deadline}'
