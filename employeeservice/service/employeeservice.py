import json

from django.contrib.auth import authenticate
from django.db.models import Q
from django.http import HttpResponse
from knox.models import AuthToken

from employeeservice.models.employeemodels import Employee, Employeedocuments
from employeeservice.data.response.employeeresponse import EmployeeResponse
from employeeservice.service.empuser import create_user
from utilityservice.data.response.empmessage import WisefinMsg, SuccessMessage, ErrorMessage, Success, SuccessStatus, Error, ErrorDescription
from utilityservice.data.response.emplist import WisefinList
from employeeservice.util.emputil import ActiveStatus, UserrefType, Grade
from utilityservice.data.response.emppaginator import WisefinPaginator


class EmployeeService:
    def create_employee(self, obj):
        resp = WisefinMsg()
        if obj.get_id() is not None:
            Employee.objects.filter(id=obj.get_id()).update(
                                                        first_name=obj.get_first_name(), middle_name=obj.get_middle_name(),
                                                        last_name=obj.get_last_name(),
                                                        email_id=obj.get_email_id(),
                                                        designation=obj.get_designation(),
                                                        doj=obj.get_doj(),
                                                        gender=obj.get_gender(),
                                                        dob=obj.get_dob(),
                                                        user_id=obj.get_user_id(),
                                                        department=obj.get_department(),
                                                        manager=obj.get_manager(),
                                                        employee_type=obj.get_employee_type(),
                                                        grade=obj.get_grade()


                                                    )
            emp_obj = Employee.objects.get(id=obj.get_id())
            resp.set_message(SuccessMessage.UPDATE_MESSAGE)


        # emp_obj = Employee.objects.filter(id=obj.get_id())
        # if len(emp_obj)==None:
        #     resp.set_message(ErrorMessage.INVALID_EMPLOYEE_ID)
        #     return resp

        # USER SERV
        # user_obj = create_user(obj.get_code())
        # user_id = user_obj['user_id']


        # if user_obj['status'] == False:
        #     return
        else:
            emp_obj = Employee.objects.create(first_name=obj.get_first_name(), middle_name=obj.get_middle_name(),
                                    last_name =obj.get_last_name(),
                                    email_id =obj.get_email_id(),
                                    designation=obj.get_designation(),
                                    doj =obj.get_doj(),
                                    gender=obj.get_gender(),
                                    dob=obj.get_dob(),
                                    user_id=obj.get_user_id(),
                                    department=obj.get_department(),
                                    manager=obj.get_manager(),
                                    employee_type=obj.get_employee_type(),
                                    grade=obj.get_grade()
                                              )

            emp_obj.code = UserrefType.EMPI + str(emp_obj.id)
            emp_obj.save()
        return emp_obj.id

#EMPLOYEE_SUMMARY_SEARCH
    def fetch_employee(self,vys_page, request):
        query = request.GET.get('query')
        code = request.GET.get('code')
        condition = Q(status=ActiveStatus.Active)
        if query is not None and query != '':
            condition &= (Q(first_name__icontains=query))
        if code is not None and code != '':
            condition &= Q(code=code)
        obj = Employee.objects.filter(condition).order_by('-created_date')[vys_page.get_offset():vys_page.get_query_limit()]
        list_data = WisefinList()
        for x in obj:
            data_resp = EmployeeResponse()
            data_resp.set_id(x.id)
            data_resp.set_code(x.code)
            data_resp.set_doj(x.doj)
            data_resp.set_dob(x.dob)
            data_resp.set_designation(x.designation)
            data_resp.set_email_id(x.email_id)
            data_resp.set_first_name(x.first_name)
            data_resp.set_middle_name(x.middle_name)
            data_resp.set_last_name(x.last_name)
            data_resp.set_gender(x.gender)
            data_resp.set_department(x.department)
            data_resp.set_manager(x.manager)
            data_resp.set_employee_type(x.employee_type)
            data_resp.set_grade(x.grade)
            list_data.append(data_resp)
        vpage = WisefinPaginator(obj, vys_page.get_index(), 10)
        list_data.set_pagination(vpage)
        return list_data

    def get_employee(self, id):
        obj = Employee.objects.get(id=id)
        data_resp = EmployeeResponse()
        data_resp.set_id(obj.id)
        data_resp.set_code(obj.code)
        data_resp.set_doj(obj.doj)
        data_resp.set_dob(obj.dob)
        data_resp.set_designation(obj.designation)
        data_resp.set_email_id(obj.email_id)
        data_resp.set_first_name(obj.first_name)
        data_resp.set_middle_name(obj.middle_name)
        data_resp.set_last_name(obj.last_name)
        data_resp.set_gender(obj.gender)
        data_resp.set_department(obj.department)
        data_resp.set_manager(obj.manager)
        data_resp.set_employee_type(obj.employee_type)
        data_resp.set_grade(obj.grade)

        return data_resp

    def del_employee(self, id):
        obj = Employee.objects.filter(id=id).update(status=ActiveStatus.Delete)
        success_obj = Success()
        success_obj.set_status(SuccessStatus.SUCCESS)
        success_obj.set_message(SuccessMessage.DELETE_MESSAGE)
        return success_obj

#FOR_APPRAISAL_CREATE_DROPDOWN
    def employee_get_info(self, id):
        obj = Employee.objects.get(id=id)
        data_resp = EmployeeResponse()
        data_resp.set_id(obj.id)
        data_resp.set_code(obj.code)
        data_resp.set_first_name(obj.first_name)
        return data_resp



#LOGIN_API
    def auth_login(self, user_name, password):
        user = authenticate(username=user_name, password=password)
        if user is None:
            resp = WisefinMsg()
            resp.set_message(ErrorMessage.INVALID_DATA)
            return resp
        else:
            token_obj = AuthToken.objects.create(user)
            emp_user = Employee.objects.filter(code=user_name)
            if len(emp_user) == 0:
                resp = WisefinMsg()
                resp.set_message(ErrorMessage.INVALID_DATA)
                return resp
            else:
                # auth_user = token_obj[0].user
                # expiry = str(token_obj[0].expiry)
                resp = WisefinMsg()
                resp.token = token_obj[1]
                # resp.name = port_user[0].name
                resp.name = emp_user[0].first_name
                resp.code = emp_user[0].code
                return resp