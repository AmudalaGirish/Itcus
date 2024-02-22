from .models import Client, Role, Employee
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

@api_view(['GET', 'POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def employee_detail(request, emp_id=None):
    if request.method == 'GET':
        employee = get_object_or_404(Employee, id=emp_id)

        employee_data = {
            'id': employee.id,
            'name': employee.name,
            'client': employee.client.name,
            'role': employee.role.name
        }
        
        return JsonResponse(employee_data)

    elif request.method == 'POST':
    
        client_name = request.data.get('client')
        role_name = request.data.get('role')

        client, _ = Client.objects.get_or_create(name=client_name)
        
        role, _ = Role.objects.get_or_create(name=role_name)

        new_employee = Employee.objects.create(
            name=request.data.get('name'),
            client=client,
            role=role
        )

        employee_data = {
            'id': new_employee.id,
            'name': new_employee.name,
            'client': new_employee.client.name,
            'role': new_employee.role.name
        }

    return JsonResponse(employee_data, status=201)
