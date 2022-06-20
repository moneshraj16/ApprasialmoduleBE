from django.db.models import Q

from employeeservice.util.emputil import ActiveStatus
from masterservice.data.response.districtresponse import DistrictResponse
from masterservice.models import District
from masterservice.util.masterutil import MasterrefType
from utilityservice.data.response.emplist import WisefinList
from utilityservice.data.response.empmessage import Success, SuccessStatus, SuccessMessage, WisefinMsg
from utilityservice.data.response.emppaginator import WisefinPaginator


class DistrictService:
    def create_district(self, district_id, data_obj):
        resp = WisefinMsg()

        if not district_id is None:
            District.objects.filter(id=district_id).update(**data_obj)
            resp.set_message(SuccessMessage.UPDATE_MESSAGE)

        else:
            obj = District.objects.create(**data_obj)
            obj.code = MasterrefType.DISTRICT + str(obj.id)
            obj.save()
            resp.set_message(SuccessMessage.CREATE_MESSAGE)
            resp.name = obj.name
            resp.code = obj.code

        return resp


    def fetch_district(self,vys_page, request):
        query = request.GET.get('query')
        condition = Q(status=ActiveStatus.Active)
        if query is not None and query != '':
            condition &= Q(name__icontains=query)
        obj = District.objects.filter(condition)[vys_page.get_offset():vys_page.get_query_limit()]
        list_data = WisefinList()
        for x in obj:
            data_resp = DistrictResponse()
            data_resp.set_id(x.id)
            data_resp.set_code(x.code)
            data_resp.set_name(x.name)
            data_resp.set_state_id(x.state_id)
            list_data.append(data_resp)
        vpage = WisefinPaginator(obj, vys_page.get_index(), 10)
        list_data.set_pagination(vpage)
        return list_data

    def get_district(self, id):
        obj = District.objects.get(id=id)
        data_resp = DistrictResponse()
        data_resp.set_id(obj.id)
        data_resp.set_code(obj.code)
        data_resp.set_name(obj.name)
        data_resp.set_state_id(obj.state_id)
        return data_resp


    def del_district(self,id):
        obj = District.objects.filter(id=id).update(status=ActiveStatus.Delete)
        success_obj = Success()
        success_obj.set_status(SuccessStatus.SUCCESS)
        success_obj.set_message(SuccessMessage.DELETE_MESSAGE)
        return success_obj

#FOR_DISTRICT_DROPDOWN
    def get_district_add(self,id):
        obj = District.objects.get(id=id)
        data_resp = DistrictResponse()
        data_resp.set_id(obj.id)
        data_resp.set_name(obj.name)
        data_resp.set_code(obj.code)
        return data_resp