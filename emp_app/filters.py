import django_filters
from .models import Employee

class EmployeeFilter(django_filters.FilterSet):
    first_name = django_filters.CharFilter(lookup_expr='icontains')
    last_name = django_filters.CharFilter(lookup_expr='icontains')
    dept = django_filters.CharFilter(field_name='dept__name', lookup_expr='icontains')
    role = django_filters.CharFilter(field_name='role__name', lookup_expr='icontains')

    class Meta:
        model = Employee
        fields = ['first_name', 'last_name', 'dept', 'role']
