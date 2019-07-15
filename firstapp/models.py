from django.db import models

# Create your models here.
class Address(models.Model):
    city=models.CharField(max_length=100)
    pincode=models.IntegerField()


class Company(models.Model):
    name=models.CharField(max_length=100)
    code=models.IntegerField()
    compAddr=models.OneToOneField(Address, on_delete=models.CASCADE, primary_key=True)


class Employee(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    salary=models.IntegerField()
    empAddr=models.ManyToManyField(Address)
    empcomp=models.ForeignKey(Company, on_delete=models.CASCADE)

