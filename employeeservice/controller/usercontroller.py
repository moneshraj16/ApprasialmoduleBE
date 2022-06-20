import json

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from rest_framework import status
from employeeservice.data.errordata import ErrorData
from employeeservice.data.request.employeerequest import EmployeeRequest
from employeeservice.data.userdata import UserData
from employeeservice.service.employeeservice import EmployeeService

#SIGNUP
@csrf_exempt
def create_user(request):
    if not request.method == 'POST':
        error_data = ErrorData()
        error_data.set_error('invalid_Request')
        return HttpResponse(error_data.get(), content_type='application/json', status=status.HTTP_400_BAD_REQUEST)

    username = None
    password = None
    emp_json = None
    user = None

    try:
        user_json = json.loads(request.body)
        username = user_json['username']
        password = user_json['password']
        emp_json = user_json['employee']

    except KeyError:
        error_data = ErrorData()
        error_data.set_error('Invalid Parameters')
        return HttpResponse(error_data.get(),content_type='application/json',status=status.HTTP_400_BAD_REQUEST)

    except:
        error_data = ErrorData()
        error_data.set_error('Invalid Parameters')

    if user is not None:
        error_data = ErrorData()
        error_data.set_error('User already exists')
        return HttpResponse(error_data.get(), content_type='application/json', status=status.HTTP_409_CONFLICT)

    else:
        user = User.objects.create_user(username=username, password=password)
        user.set_password(password)
        user.save()
        emp_req = EmployeeRequest(emp_json)
        emp_req.set_user_id(user.id)
        employee_service = EmployeeService()
        employee_service.create_employee(emp_req)
        user_data = UserData()
        user_data.set_id(user.id)
        user_data.set_username(user.username)
        return HttpResponse(user_data.get(), content_type='application/json', status=status.HTTP_200_OK)