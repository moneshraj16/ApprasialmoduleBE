import json

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view

from masterservice.data.request.cityrequest import CityRequest
from masterservice.data.request.countryrequest import CountryRequest
from masterservice.data.request.departementrequest import DepartmentRequest
from masterservice.data.request.designationrequest import DesignationRequest
from masterservice.data.request.districtrequest import DistrictRequest
from masterservice.data.request.goalmappingrequest import GoalMappingRequest
from masterservice.data.request.goalrequest import GoalRequest
from masterservice.data.request.pincoderequest import PincodeRequest
from masterservice.data.request.staterequest import StateRequest
from masterservice.service.cityservice import CityService
from masterservice.service.countryservice import CountryService
from masterservice.service.departementservice import DepartmentService
from masterservice.service.designationservice import DesignationService
from masterservice.service.districtservice import DistrictService
from masterservice.service.goalmappingservice import GoalMappingService
from masterservice.service.goalservice import GoalService
from masterservice.service.pincodeservice import PincodeService
from masterservice.service.stateservice import StateService
from utilityservice.data.response.emppage import WisefinPage


@csrf_exempt
@api_view(['POST', 'GET'])
def create_department(request):
    if request.method == 'POST':
        data_json = json.loads(request.body)
        request_fn = DepartmentRequest()
        dep_id = request_fn.fetch_id(data_json)
        req_dict = request_fn.fetch_request(data_json)
        req_obj = DepartmentService().create_department(req_dict, dep_id)
        response = HttpResponse(req_obj.get(), content_type='application/json')
        return response

    elif request.method == 'GET':
        page = request.GET.get('page', 1)
        page = int(page)
        vys_page = WisefinPage(page, 10)
        req_obj = DepartmentService().fetch_department(vys_page, request)
        response = HttpResponse(req_obj.get(), content_type='application/json')
        return response

@csrf_exempt
@api_view(['GET','DELETE'])
def get_department(request, id):
    if request.method == 'GET':
        req_obj = DepartmentService().get_department(id)
        response = HttpResponse(req_obj.get(), content_type='application/json')
        return response

    elif request.method == 'DELETE':
        req_obj = DepartmentService().del_department(id)
        response = HttpResponse(req_obj.get(), content_type='application/json')
        return response

#COUNTRY
@csrf_exempt
@api_view(['POST', 'GET'])
def country(request):
    if request.method == 'POST':
        data_json = json.loads(request.body)
        request_fn = CountryRequest()
        country_id = request_fn.fetch_id(data_json)
        req_dict = request_fn.fetch_request(data_json)
        req_obj = CountryService().create_country(country_id, req_dict)
        response = HttpResponse(req_obj.get(), content_type='application/json')
        return response

    elif request.method == 'GET':
        page = request.GET.get('page', 1)
        page = int(page)
        vys_page = WisefinPage(page, 10)
        resp_obj = CountryService().fetch_country(vys_page,request)
        response = HttpResponse(resp_obj.get(),content_type='application/json')
        return response


@csrf_exempt
@api_view(['GET', 'DELETE'])
def get_country(request, id):
    if request.method == 'GET':
        resp_obj = CountryService().get_country(id)
        response = HttpResponse(resp_obj.get(), content_type='application/json')
        return response

    elif request.method == 'DELETE':
        resp_obj = CountryService().del_country(id)
        response = HttpResponse(resp_obj.get(), content_type='application/json')
        return response


#STATE
@csrf_exempt
@api_view(['POST','GET'])
def state(request):
    if request.method == 'POST':
        data_json = json.loads(request.body)
        request_fn = StateRequest()
        state_id = request_fn.fetch_id(data_json)
        req_dict = request_fn.fetch_request(data_json)
        req_obj = StateService().create_state(state_id, req_dict)
        response = HttpResponse(req_obj.get(), content_type='application/json')
        return response

    elif request.method == 'GET':
        page = request.GET.get('page', 1)
        page = int(page)
        vys_page = WisefinPage(page, 10)
        req_obj = StateService().fetch_state(vys_page,request)
        response = HttpResponse(req_obj.get(), content_type='application/json')
        return response

@csrf_exempt
@api_view(['GET','DELETE'])
def get_state(request, id):
    if request.method == 'GET':
        req_obj = StateService().get_state(id)
        response = HttpResponse(req_obj.get(), content_type='application/json')
        return response

    elif request.method == 'DELETE':
        req_obj = StateService().del_state(id)
        response = HttpResponse(req_obj.get(), content_type='application/json')
        return response


#DISTRICT
@csrf_exempt
@api_view(['POST','GET'])
def district(request):
    if request.method == 'POST':
        data_json = json.loads(request.body)
        request_fn = DistrictRequest()
        district_id = request_fn.fetch_id(data_json)
        req_dict = request_fn.fetch_request(data_json)
        req_obj = DistrictService().create_district(district_id, req_dict)
        response = HttpResponse(req_obj.get(), content_type='application/json')
        return response

    elif request.method == 'GET':
        page = request.GET.get('page', 1)
        page = int(page)
        vys_page = WisefinPage(page, 10)
        req_obj = DistrictService().fetch_district(vys_page, request)
        response = HttpResponse(req_obj.get(), content_type='application/json')
        return response

@csrf_exempt
@api_view(['GET','DELETE'])
def get_district(request, id):
    if request.method == 'GET':
        req_obj = DistrictService().get_district(id)
        response = HttpResponse(req_obj.get(), content_type='application/json')
        return response

    elif request.method == 'DELETE':
        req_obj = DistrictService().del_district(id)
        response = HttpResponse(req_obj.get(), content_type='application/json')
        return response


#CITY

@csrf_exempt
@api_view(['POST','GET'])
# @authentication_classes([VowAuthentication])
# @permission_classes([IsAuthenticated, VowPermission])
def city(request):
    if request.method == 'POST':
        data_json = json.loads(request.body)
        request_fn = CityRequest()
        city_id = request_fn.fetch_id(data_json)
        req_dict = request_fn.fetch_request(data_json)
        req_obj = CityService().create_city(city_id,req_dict)
        response = HttpResponse(req_obj.get(), content_type='application/json')
        return response

    elif request.method == 'GET':
        page = request.GET.get('page', 1)
        page = int(page)
        vys_page = WisefinPage(page, 10)
        req_obj = CityService().fetch_city(vys_page, request)
        response = HttpResponse(req_obj.get(), content_type='application/json')
        return response


@csrf_exempt
@api_view(['GET','DELETE'])
# @authentication_classes([VowAuthentication])
# @permission_classes([IsAuthenticated, VowPermission])
def get_city(request, id):
    if request.method == 'GET':
        req_obj = CityService().get_city(id)
        response = HttpResponse(req_obj.get(), content_type='application/json')
        return response

    elif request.method == 'DELETE':
        req_obj = CityService().del_city(id)
        response = HttpResponse(req_obj.get(), content_type='application/json')
        return response

#PINCODE
@csrf_exempt
@api_view(['POST','GET'])
# @authentication_classes([VowAuthentication])
# @permission_classes([IsAuthenticated, VowPermission])
def pincode(request):
    if request.method == 'POST':
        data_json = json.loads(request.body)
        request_fn = PincodeRequest()
        pincode_id = request_fn.fetch_id(data_json)
        req_dict = request_fn.fetch_request(data_json)
        req_obj = PincodeService().create_pincode(pincode_id, req_dict)
        response = HttpResponse(req_obj.get(), content_type='application/json')
        return response

    elif request.method == 'GET':
        page = request.GET.get('page', 1)
        page = int(page)
        vys_page = WisefinPage(page, 10)
        req_obj = PincodeService().fetch_pincode(vys_page,request)
        response = HttpResponse(req_obj.get(), content_type='application/json')
        return response

@csrf_exempt
@api_view(['GET'])
def get_pincode_searchlist(request):
    if request.method == 'GET':
        search = request.GET.get('query', None)
        page = request.GET.get('page', 1)
        page = int(page)
        vys_page = WisefinPage(page, 10)
        if search.isnumeric() or search == '':
            pincode_service = PincodeService()
            resp_obj = pincode_service.fetch_pincode_search(search, vys_page)
            response = HttpResponse(resp_obj.get(), content_type='application/json')
            return response

    # else:
    #     pincode_service = PincodeService()
    #     resp_obj = pincode_service.fetch_pincode_city(search, vys_page)
    #     response = HttpResponse(resp_obj.get(), content_type='application/json')
    #     return response





@csrf_exempt
@api_view(['GET', 'DELETE'])
# @authentication_classes([VowAuthentication])
# @permission_classes([IsAuthenticated, VowPermission])
def get_pincode(request, id):
    if request.method == 'GET':
        req_obj = PincodeService().get_pincode(id)
        response = HttpResponse(req_obj.get(), content_type='application/json')
        return response

    elif request.method == 'DELETE':
        req_obj = PincodeService().del_pincode(id)
        response = HttpResponse(req_obj.get(), content_type='application/json')
        return response

#GOAL
@csrf_exempt
@api_view(['POST', 'GET'])
def goal(request):
    if request.method == 'POST':
        data_json = json.loads(request.body)
        request_fn = GoalRequest()
        goal_id = request_fn.fetch_id(data_json)
        req_dict = request_fn.fetch_request(data_json)
        req_obj = GoalService().create_goal(req_dict, goal_id)
        response = HttpResponse(req_obj.get(), content_type='application/json')
        return response

    elif request.method == 'GET':
        page = request.GET.get('page', 1)
        page = int(page)
        vys_page = WisefinPage(page, 10)
        req_obj = GoalService().fetch_goal(vys_page,request)
        response = HttpResponse(req_obj.get(), content_type='application/json')
        return response

@csrf_exempt
@api_view(['GET', 'DELETE'])
def get_goal(request, id):
    if request.method == 'GET':
        req_obj = GoalService().get_goal(id)
        response = HttpResponse(req_obj.get(), content_type='application/json')
        return response

    elif request.method == 'DELETE':
        req_obj = GoalService().del_goal(id)
        response = HttpResponse(req_obj.get(), content_type='application/json')
        return response


#DESIGNATION
@csrf_exempt
@api_view(['POST','GET'])
def create_designation(request):
    if request.method == 'POST':
        data_json = json.loads(request.body)
        request_fn = DesignationRequest()
        designation_id = request_fn.fetch_id(data_json)
        req_dict = request_fn.fetch_request(data_json)
        req_obj = DesignationService().create_designation(designation_id, req_dict)
        response = HttpResponse(req_obj.get(), content_type='application/json')
        return response
    elif request.method == 'GET':
        page = request.GET.get('page', 1)
        page = int(page)
        vys_page = WisefinPage(page, 10)
        req_obj = DesignationService().fetch_designation(vys_page, request)
        response = HttpResponse(req_obj.get(), content_type='application/json')
        return response

@csrf_exempt
@api_view(['GET', 'DELETE'])
def get_designation(request, id):
    if request.method == 'GET':
        req_obj = DesignationService().get_designation(id)
        response = HttpResponse(req_obj.get(), content_type='application/json')
        return response

    elif request.method == 'DELETE':
        req_obj = DesignationService().del_designation(id)
        response = HttpResponse(req_obj.get(), content_type='application/json')
        return response


#FOR_GOAL_EDIT_SCREEN
@csrf_exempt
@api_view(['GET'])
def goal_get(request, id):
    if request.method == 'GET':
        goal_serv = GoalService()
        resp_obj = goal_serv.goal_get(id)
        response = HttpResponse(resp_obj.get(), content_type='application/json')
        return response

#GOAL_MAPPING_TABLE
@csrf_exempt
@api_view(['POST', 'GET'])
def create_goal_mapping(request):
    if request.method == 'POST':
        data_json = json.loads(request.body)
        request_fn = GoalMappingRequest(data_json)
        val = data_json['sub_goal']
        for x in val:
            req_obj = GoalMappingService().create_goal_mapping(request_fn, x['description'])
        response = HttpResponse(req_obj.get(), content_type='application/json')
        return response

    elif request.method == 'GET':
        page = request.GET.get('page', 1)
        page = int(page)
        vys_page = WisefinPage(page, 10)
        req_obj = GoalMappingService().fetch_goal_mapping(vys_page, request)
        response = HttpResponse(req_obj.get(), content_type='application/json')
        return response


@csrf_exempt
@api_view(['GET', 'DELETE'])
def get_goal_mapping(request, id):
    if request.method == 'GET':
        req_obj = GoalMappingService().get_goal_mapping(id)
        response = HttpResponse(req_obj.get(), content_type='application/json')
        return response

    elif request.method == 'DELETE':
        req_obj = GoalMappingService().del_goal_mapping(id)
        response = HttpResponse(req_obj.get(), content_type='application/json')
        return response
