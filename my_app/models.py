from django.db import models


class TestModel(models.Model):
    string = models.CharField(max_length=20, verbose_name="Название поля 1")
    date = models.DateField(verbose_name="Дата 1")
    datetime = models.DateTimeField(verbose_name="Дата и время 1")
    checkbox = models.BooleanField(verbose_name="Чек бокс 1")
    integer = models.IntegerField(verbose_name="Число 1")
    choices = models.IntegerField(verbose_name="Выборка", choices=(
        (1, 'One'),
        (2, 'Two'),
        (3, 'Three'),
    ))
    nullable = models.TextField(verbose_name="Какой-то текст", blank=True, null=True)

    def __str__(self):
        return f'Тестовая модель №{self.id}'
