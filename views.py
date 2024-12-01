from django.shortcuts import render
from django.http import JsonResponse
from .models import DynamicField, Employee
import json
# Create your views here.

def dynamic_fields(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        field = DynamicField(label=data['label'], field_type=data['field_type'])
        field.save()
        return JsonResponse({'message': 'Field created successfully'}, status=201)

    fields = DynamicField.objects.values()
    return JsonResponse(list(fields), safe=False)

def employee_management(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        employee = Employee(name=data['name'], dynamic_data=data['dynamic_data'])
        employee.save()
        return JsonResponse({'message': 'Employee created successfully'}, status=201)

    employees = Employee.objects.values()
    return JsonResponse(list(employees), safe=False)
