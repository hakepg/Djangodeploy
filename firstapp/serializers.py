from .models import *
from rest_framework.serializers import ModelSerializer

class AdreesSerializer(ModelSerializer):
    class Meta:
        model=Address
        fields='__all__'
        

class CompanySerializer(ModelSerializer):
    class Meta:
        model= Company
        fields='__all__'


class EmployeSerializer(ModelSerializer):
    class Meta:
        model= Employee
        fields='__all__'