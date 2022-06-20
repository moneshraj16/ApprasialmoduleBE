from django.db.models import Q

from employeeservice.util.emputil import ActiveStatus
from masterservice.data.response.cityresponse import CityResponse
from masterservice.models import City
from masterservice.util.masterutil import MasterrefType
from utilityservice.data.response.emplist import WisefinList
from utilityservice.data.response.empmessage import WisefinMsg, SuccessMessage, Success, SuccessStatus
from utilityservice.data.response.emppaginator import WisefinPaginator


class CityService:
    def create_city(self, city_id, data_obj):
        resp = WisefinMsg()

        if not city_id is None:
            City.objects.filter(id=city_id).update(**data_obj)
            resp.set_message(SuccessMessage.UPDATE_MESSAGE)

        else:
            obj = City.objects.create(**data_obj)
            obj.code = MasterrefType.CITY + str(obj.id)
            obj.save()
            resp.set_message(SuccessMessage.CREATE_MESSAGE)
            resp.name = obj.name
            resp.code = obj.code

        return resp


    def fetch_city(self,vys_page,request):
        query = request.GET.get('query')
        condtion = Q(status=ActiveStatus.Active)
        if query is not None and query !='':
            condtion &= Q(name__icontains=query)
        obj = City.objects.filter(condtion)[vys_page.get_offset():vys_page.get_query_limit()]
        list_data = WisefinList()
        for x in obj:
            data_resp = CityResponse()
            data_resp.set_id(x.id)
            data_resp.set_name(x.name)
            data_resp.set_code(x.code)
            data_resp.set_state_id(x.state_id)
            list_data.append(data_resp)
        vpage = WisefinPaginator(obj, vys_page.get_index(), 10)
        list_data.set_pagination(vpage)
        return list_data

    def get_city(self,id):
        obj = City.objects.get(id=id)
        data_resp = CityResponse()
        data_resp.set_id(obj.id)
        data_resp.set_name(obj.name)
        data_resp.set_code(obj.code)
        data_resp.set_state_id(obj.state_id)
        return data_resp


    def del_city(self,id):
        obj = City.objects.filter(id=id).update(status=ActiveStatus.Delete)
        success_obj = Success()
        success_obj.set_message(SuccessMessage.DELETE_MESSAGE)
        success_obj.set_status(SuccessStatus.SUCCESS)
        return success_obj

    def get_city_add(self, id):
        obj = City.objects.get(id=id)
        data_resp = CityResponse()
        data_resp.set_id(obj.id)
        data_resp.set_name(obj.name)
        data_resp.set_code(obj.code)
        return data_resp