import json

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, authentication_classes, permission_classes

from employeeservice.models import Employee, EmployeeAddress
from employeeservice.service.employeeeducationservice import EmployeeEducationService
# from employeeservice.util.emputil import get_fileextension_val
from employeeservice.util import emputil
from utilityservice.data.response.emppage import WisefinPage
from employeeservice.data.request.employeerequest import EmployeeRequest
from employeeservice.data.request.employeeaddressrequest import EmployeeAddressRequest
from employeeservice.data.request.employeeeducationrequest import EmployeeEducationRequest
from employeeservice.service.employeeservice import EmployeeService
from employeeservice.service.employeeaddressservice import EmployeeAddressService
from emputilityservice.service.authentication import EmployeeAuthentication
from rest_framework.permissions import IsAuthenticated
from emputilityservice.service.permission import EmployeePermission
from employeeservice.data.request.employeeexprequest import EmployeeExpRequest
from employeeservice.service.employeeexpservice import EmployeeExpService
from employeeservice.data.request.employeepersonalinforequest import EmployeePersonalinfoRequest
from employeeservice.service.employeepersonalinfoservice import EmployeePersonalinfoService
from utilityservice.data.response.empmessage import WisefinMsg, SuccessMessage, ErrorMessage, Success, SuccessStatus, Error, ErrorDescription
from employeeservice.data.request.employeedocumentrequest import EmployeeDocumentRequest
from employeeservice.service.employeedocumentservice import EmployeeDocumentService
from employeeservice.util.emputil import employee_type_compostie, employee_type_val, grade_type_val, \
    grade_type_compostie, document_upload


@csrf_exempt
@api_view(['POST', 'GET'])
# @authentication_classes([EmployeeAuthentication])
# @permission_classes([IsAuthenticated, EmployeePermission])
def create_employee(request):
    if request.method == 'POST':
        data_json = json.loads(request.data.dict().get('data'))
        # files = request.FILES.get('file')
        # data_json = json.loads(request.body)
        request_fn = EmployeeRequest(data_json)
        employee_address = EmployeeAddressService()
        employee_education = EmployeeEducationService()
        employee_experience = EmployeeExpService()
        employee_personalinfo = EmployeePersonalinfoService()
        employee_document = EmployeeDocumentService()
        emp_id = EmployeeService().create_employee(request_fn)
        #employee_address
        if emp_id:
            address = data_json.get('address')
            print('address_id', address)
            address_obj = EmployeeAddressRequest()
            addr_data = address_obj.fetch_request(address, emp_id)
            addr_obj = address_obj.fetch_id(data_json)
        #employee_education
            education = data_json.get('education')
            print('education_id', education)
            education_obj = EmployeeEducationRequest()
            edu_data = education_obj.fetch_request(education, emp_id)
            edu_obj = education_obj.fetch_id(data_json)
        #employee_experience
            experience = data_json.get('experience')
            print('experience_id', experience)
            experience_obj = EmployeeExpRequest()
            exp_data = experience_obj.fetch_request(experience, emp_id)
            exp_obj = experience_obj.fetch_id(data_json)
        #employee_personalinfo
            personal_info = data_json.get('personal_info')
            print('personal_id', personal_info)
            personal_info_obj = EmployeePersonalinfoRequest()
            per_data = personal_info_obj.fetch_request(personal_info, emp_id)
            per_obj = personal_info_obj.fetch_id(data_json)
            # emp_doc = data_json.get('document')
        # print('document', emp_doc)
        # document_resp = EmployeeDocumentRequest(emp_doc)


        if emp_id != None:
            address_obj = employee_address.create_emp_address(addr_data, addr_obj)
            education_obj = employee_education.create_emp_edu(edu_data, edu_obj)
            experience_obj = employee_experience.create_employee_exp(exp_data, exp_obj)
            personalinfo_obj = employee_personalinfo.create_personalinfo(per_data, per_obj)
            # files = {'file':'1'}
            document_obj = employee_document.create_empdocument(request, emp_id)
            resp = WisefinMsg()
            resp.set_message(SuccessMessage.CREATE_MESSAGE)
            response = HttpResponse(resp.get(), content_type='application/json')
            return response
        else:
            resp = WisefinMsg()
            resp.set_message(ErrorMessage.INVALID_DATA)
            response = HttpResponse(resp.get(), content_type='application/json')
            return response


    elif request.method == 'GET':
        page = request.GET.get('page', 1)
        page =int(page)
        vys_page = WisefinPage(page, 10)
        req_obj = EmployeeService().fetch_employee(vys_page, request)
        response = HttpResponse(req_obj.get(), content_type='application/json')
        return response

@csrf_exempt
@api_view(['GET', 'DELETE'])
def get_employee(request, id):
    if request.method == 'GET':
        req_obj = EmployeeService().get_employee(id)
        response = HttpResponse(req_obj.get(), content_type='application/json')
        return response
    elif request.method == 'DELETE':
        req_obj = EmployeeService().del_employee(id)
        response = HttpResponse(req_obj.get(), content_type='application/json')
        return response

#EMPLOYEE_ADDRESS
@csrf_exempt
@api_view(['POST', 'GET'])
def create_employee_addr(request, employee_id):
    if request.method == 'POST':
        data_json = json.loads(request.body)
        request_fn = EmployeeAddressRequest()
        emp_add_id = request_fn.fetch_id(data_json)
        req_dict = request_fn.fetch_request(data_json, employee_id)
        resp_obj = EmployeeAddressService().create_emp_address(req_dict, emp_add_id)
        response = HttpResponse(resp_obj.get(), content_type='application/json')
        return response

    elif request.method == 'GET':
        # page = request.GET.get('page', 1)
        # page = int(page)
        # vys_page = WisefinPage(page, 10)
        res_obj = EmployeeAddressService().fetch_employee_addr(employee_id)
        response = HttpResponse(res_obj.get(), content_type='application/json')
        return response

@csrf_exempt
@api_view(['GET', 'DELETE'])
def get_employee_addr(request, id):
    if request.method == 'GET':
        req_obj = EmployeeAddressService().get_employee_addr(id)
        response = HttpResponse(req_obj.get(), content_type='application/json')
        return response
    elif request.method == 'DELETE':
        req_obj = EmployeeAddressService().del_employee_addr(id)
        response = HttpResponse(req_obj.get(), content_type='application/json')
        return response

#EMPLOYEE_EDUCATION
@csrf_exempt
@api_view(['POST', 'GET'])
def create_employee_edu(request, employee_id):
    if request.method == 'POST':
        data_json = json.loads(request.body)
        request_fn = EmployeeEducationRequest()
        emp_edu_id = request_fn.fetch_id(data_json)
        req_dict = request_fn.fetch_request(data_json, employee_id)
        req_obj = EmployeeEducationService().create_emp_edu(req_dict, emp_edu_id)
        response = HttpResponse(req_obj.get(), content_type='application/json')
        return response
    elif request.method == 'GET':
        # page = request.GET.get('page', 1)
        # page = int(page)
        # vys_page = WisefinPage(page, 10)
        req_obj = EmployeeEducationService().fetch_emp_edu(employee_id)
        response = HttpResponse(req_obj.get(), content_type='application/json')
        return response

@csrf_exempt
@api_view(['GET', 'DELETE'])
def get_employee_edu(request, id):
    if request.method == 'GET':
        req_obj = EmployeeEducationService().get_employee_edu(id)
        response = HttpResponse(req_obj.get(), content_type='application/json')
        return response

    elif request.method == 'DELETE':
        req_obj = EmployeeEducationService().del_employee_edu(id)
        response = HttpResponse(req_obj.get(), content_type='application/json')
        return response

#EMPLOYEE_EXPERIRENCE
@csrf_exempt
@api_view(['POST','GET'])
def create_employee_exp(request, employee_id):
    if request.method == 'POST':
        data_json = json.loads(request.body)
        request_fn = EmployeeExpRequest()
        employee_exp_id = request_fn.fetch_id(data_json)
        req_dict = request_fn.fetch_request(data_json, employee_id)
        req_obj = EmployeeExpService().create_employee_exp(req_dict, employee_exp_id)
        response = HttpResponse(req_obj.get(), content_type='application/json')
        return response

    elif request.method == 'GET':
        # page = request.GET.get('page', 1)
        # page = int(page)
        # vys_page = WisefinPage(page, 10)
        req_obj = EmployeeExpService().fetch_employeexp(employee_id)
        response = HttpResponse(req_obj.get(), content_type='application/json')
        return response

@csrf_exempt
@api_view(['GET', 'DELETE'])
def get_employee_exp(request, id):
    if request.method == 'GET':
        req_obj = EmployeeExpService().get_employee_exp(id)
        response = HttpResponse(req_obj.get(), content_type='application/json')
        return response
    elif request.method == 'DELETE':
        req_obj = EmployeeExpService().del_employee_exp(id)
        response = HttpResponse(req_obj.get(), content_type='application/json')
        return response

#EMPLOYEE_PERSONAL_INFO
@csrf_exempt
@api_view(['POST', 'GET'])
def create_emp_personalinfo(request, employee_id):
    if request.method == 'POST':
        data_json = json.loads(request.body)
        request_fn = EmployeePersonalinfoRequest()
        personalinfo_id = request_fn.fetch_id(data_json)
        req_dict = request_fn.fetch_request(data_json, employee_id)
        req_obj = EmployeePersonalinfoService().create_personalinfo(req_dict, personalinfo_id)
        response = HttpResponse(req_obj.get(), content_type='application/json')
        return response

    elif request.method == 'GET':
        # page = request.GET.get('page', 1)
        # page = int(page)
        # vys_page = WisefinPage(page, 10)
        req_obj = EmployeePersonalinfoService().fetch_personalinfo(employee_id)
        response = HttpResponse(req_obj.get(), content_type='application/json')
        return response

@csrf_exempt
@api_view(['GET', 'DELETE'])
def get_employee_perinfo(request, id):
    if request.method == 'GET':
        req_obj = EmployeePersonalinfoService().get_employee_perinfo(id)
        response = HttpResponse(req_obj.get(), content_type='application/json')
        return response

    elif request.method == 'DELETE':
        req_obj = EmployeePersonalinfoService().del_employee_perinfo(id)
        response = HttpResponse(req_obj.get(), content_type='application/json')
        return response

#EMPLOYEE_DOC_ATTACHMENT
@csrf_exempt
@api_view(['POST', 'GET'])
def create_employee_doc(request, employee_id):
    if request.method == 'POST':
        # data_json = json.loads(request.body)
        doc_service = EmployeeDocumentService()
        data_json = json.loads(request.data.dict().get('data'))
        files = request.FILES.get('file')
        resp_obj = doc_service.create_empdocument(request, employee_id)
        response = HttpResponse(resp_obj.get(), content_type='application/json')
        return response

    elif request.method == 'GET':
        page = request.GET.get('page', 1)
        page = int(page)
        vys_page = WisefinPage(page, 10)
        req_obj = EmployeeDocumentService().fetch_empdoument(vys_page, employee_id)
        response = HttpResponse(req_obj.get(), content_type='application/json')
        return response


#EMPLOYEE_DOC_DEL AND CREATE_ATTACHMENT
@csrf_exempt
@api_view(['POST', 'DELETE'])
def get_employee_doc(request, employee_id):
    if request.method == 'POST':
        req_obj = EmployeeDocumentService().create_empdocuments(request, employee_id)
        response = HttpResponse(req_obj.get(), content_type='application/json')
        return response


#DELETE_ATTACHMENT
@csrf_exempt
@api_view(['DELETE'])
def del_emloyee_doc(request, id):
    if request.method == 'DELETE':
        req_obj = EmployeeDocumentService().del_empdocument(id)
        response = HttpResponse(req_obj.get(), content_type='application/json')
        return response


#GET_API_FOR_EMPLOYEE_DETAILS
@csrf_exempt
@api_view(['GET'])
def employee_get(request, employee_id):
    if request.method == 'GET':
        employee_serv = EmployeeService()
        address_serv = EmployeeAddressService()
        emp_edu_serv = EmployeeEducationService()
        emp_exp_serv = EmployeeExpService()
        emp_perinfo_serv = EmployeePersonalinfoService()
        emp_doc_serv = EmployeeDocumentService()
        emp_id = Employee.objects.filter(id=employee_id)

        if len(emp_id) > 0:
           employee = employee_serv.get_employee(emp_id[0].id)
           emp_addr = address_serv.fetch_employee_addres(employee_id)
           employee.address = emp_addr
           emp_edu = emp_edu_serv.fetch_emp_education(employee_id)
           employee.education = emp_edu
           emp_exp = emp_exp_serv.fetch_employeexperience(employee_id)
           employee.experience = emp_exp
           emp_perinfo = emp_perinfo_serv.fetch_personalinformation(employee_id)
           employee.personal_info = emp_perinfo
           emp_document = emp_doc_serv.get_document(employee_id)
           employee.document = emp_document
           response = HttpResponse(employee.get(), content_type='application/json')
           return response

        else:
            resp = Error()
            resp.set_description(ErrorMessage.INVALID_DATA)
            resp.set_code('400')
            response = HttpResponse(resp.get(), content_type='application/json')
            return response


#EMPLOYEE_VIEW_FILE
@csrf_exempt
@api_view(['GET'])
def emp_view_file(request, file_id):
    if request.method == 'GET':
        attachment_serv = EmployeeDocumentService()
        file_doc = attachment_serv.file_view(file_id)
        return file_doc

#EMPLOYEE_FILE_GET
@csrf_exempt
@api_view(['GET'])
def emp_file_get(request, employee_id):
    if request.method == 'GET':
        doc_serv = EmployeeDocumentService()
        req_obj = doc_serv.get_documents(employee_id)
        res_val = json.dumps(req_obj)
        response = HttpResponse(res_val, content_type='application/json')
        return response


#EMPLOYEE_TYPE_DROPDOWN
@csrf_exempt
@api_view(['GET'])
def get_employee_dropdown(request):
    if request.method == 'GET':
        req_obj = employee_type_compostie()
        response = HttpResponse(req_obj.get(), content_type='application/json')
        return response

#EMPLOYEE_TYPE_GET
@csrf_exempt
@api_view(['GET'])
def employee_type_get(request, type_id):
    if request.method == 'GET':
        type_id = int(type_id)
        req_obj = employee_type_val(type_id)
        response = HttpResponse(req_obj.get(), content_type='application/json')
        return response

#EMPLOYEE_FILE_DOWNLODE
@csrf_exempt
@api_view(['GET'])
def employee_file_download(request, file_id):
    if request.method == 'GET':
        req_obj = EmployeeDocumentService().employee_file_download(file_id)
        response = HttpResponse(req_obj, content_type='application/json')
        return response

#EMPLOYEE_GRADE_DROPDOWN
@csrf_exempt
@api_view(['GET'])
def get_grade(request, id):
    if request.method == 'GET':
        id = int(id)
        req_obj = grade_type_val(id)
        response = HttpResponse(req_obj.get(),content_type='application/json')
        return response

#FETCHING_EMPLOYEE_GRADE_DROPDOWN
@csrf_exempt
@api_view(['GET'])
def fetch_grade(request):
    if request.method == 'GET':
        val = grade_type_compostie()
        response = HttpResponse(val.get(), content_type='application/json')
        return response

@csrf_exempt
def auth_token(request):
    resp_obj = json.loads(request.body)
    code = resp_obj['code']
    password = resp_obj['password']
    Emp_service = EmployeeService()
    portal_response = Emp_service.auth_login(code, password)
    response = HttpResponse(portal_response.get(), content_type="application/json")
    return response
