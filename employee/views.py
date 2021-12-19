from django.shortcuts import render
from django.views.generic import ListView
from rest_framework.filters import OrderingFilter
from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from django_filters.rest_framework import DjangoFilterBackend

from .models import Employee
from .serializers import EmployeeSerializers
from .service import EmployeeFilter
# Create your views here.

class EmployeeViewSet(mixins.UpdateModelMixin,mixins.RetrieveModelMixin,mixins.ListModelMixin,mixins.CreateModelMixin,mixins.DestroyModelMixin,GenericViewSet):
    serializer_class = EmployeeSerializers
    filter_backends = (DjangoFilterBackend,OrderingFilter)
    filter_class = EmployeeFilter
    ordering_fields = ['name','surname','patronymic','position','employment_date','salary','parent']
    queryset = Employee.objects.all()

    def perform_create(self, serializer):
        name = self.request.name
        serializer.save(author=name)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)