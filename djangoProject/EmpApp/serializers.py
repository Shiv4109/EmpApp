from rest_framework import serializers
from EmpApp.models import Employees,Departments,Projects,Manager

class EmployeesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Employees
        fields= '_all_'

class DepartmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Departments
        fields= '_all_'

class ProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Projects
        fields= '_all_'

class ManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Manager
        fields= '_all_'