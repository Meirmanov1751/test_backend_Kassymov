from django_filters import rest_framework as filters
from .models import Employee




class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    pass


class EmployeeFilter(filters.FilterSet):
    name = filters.CharFilter()
    surname = filters.CharFilter()
    patronymic = filters.CharFilter()
    position = filters.CharFilter()
    employment_date = filters.DateFilter()
    salary = filters.RangeFilter()
    parent = CharFilterInFilter(field_name='parent__name',lookup_expr='in')

    class Meta:
        model = Employee
        fields = ['name','surname','patronymic','position','employment_date','salary','parent']

