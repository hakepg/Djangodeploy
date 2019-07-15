from django.shortcuts import render
from .models import *
from firstapp.serializers import *
from rest_framework.viewsets import ModelViewSet
# Create your views here.

class AddressViewset(ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AdreesSerializer


class CompanyViewset(ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class EmployeViewset(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeSerializer