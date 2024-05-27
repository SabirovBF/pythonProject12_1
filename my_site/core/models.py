from django.db import models
from django.db.models import CharField


class Grade(models.Model):
    name = models.CharField('Уровень', max_length=255)

    class Meta:
        verbose_name = 'Уровень'
        verbose_name_plural = 'Уровни'

    def __str__(self) -> str:
        return self.name


class Programmer(models.Model):
    surname = models.CharField('Фамилия', max_length=50)
    name = models.CharField('Имя', max_length=50)
    patronymic = models.CharField('Отчество', max_length=50, blank=True)

    birthday = models.DateField('Дата рождения')
    photo = models.ImageField('Аватар', upload_to='photos/', blank=True, null=True)
    salary = models.DecimalField('Заработная плата', max_digits=10, decimal_places=2)
    is_teamlead = models.BooleanField('Тимлид', default=False)
    drade = models.ForeignKey(Grade, related_name='programmers', verbose_name='Уровень', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Программист'
        verbose_name_plural = 'Программисты'
        ordering = ('surname', 'name', 'patronymic')

    def __str__(self) -> str:
        return self.name

    def get_full_name(self) -> str:
        name = f'{self.surname} {self.name}'
        name += f' {self.patronymic}' if self.patronymic else ''

        return name
