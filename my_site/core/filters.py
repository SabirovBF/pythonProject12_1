import django_filters
from django.db.models import Q

from core import models


class Programmer(django_filters.FilterSet):
    name = django_filters.CharFilter(label='Имя', lookup_expr='icontains')
    birthday_to = django_filters.DateFilter(label='День рождения по', field_name='birthday', lookup_expr='lt')
    salary_from = django_filters.NumberFilter(label='Зарплата до', field_name='salary', lookup_expr='gte')

    fio = django_filters.CharFilter(label='ФИО', method='fio_filter')

    class Meta:
        model = models.Programmer
        exclude = ('photo', )

    def fio_filter(self, queryset, name, value):
        return queryset.filter(Q(name__icontains=value) | Q(surname__icontains=value) | Q(patronymic__icontains=value))