from django.db import models

# Create your models here.


class ToDo(models.Model):
    title = models.CharField('Название задачи', max_length=200)
    is_completed = models.BooleanField('Завершено', default=False)


    class Meta:
        verbose_name = 'Задание'
        verbose_name_plural = 'Задания'

    def __str__(self):
        return self.title
