from django.db.models import Q

from employeeservice.util.emputil import ActiveStatus
from masterservice.data.response.pincoderesponse import PincodeResponse
from masterservice.data.response.pincodesearchresponse import PincodeSearchResponse
from masterservice.models import Pincode, City
from utilityservice.data.response.emplist import WisefinList
from utilityservice.data.response.empmessage import WisefinMsg, SuccessMessage, Success, SuccessStatus
from utilityservice.data.response.emppaginator import WisefinPaginator


class PincodeService:
    def create_pincode(self,pincode_id,data_obj):
        resp = WisefinMsg()
        if not pincode_id is None:
            Pincode.objects.filter(id=pincode_id).update(**data_obj)
            resp.set_message(SuccessMessage.UPDATE_MESSAGE)

        else:
            Pincode.objects.create(**data_obj)
            resp.set_message(SuccessMessage.CREATE_MESSAGE)
        return resp


    def fetch_pincode(self,vys_page, request):
        query = request.GET.get('query')
        condtion = Q(status=ActiveStatus.Active)
        if query is not None and query != '':
            condtion &= Q(no__icontains=query)
        obj = Pincode.objects.filter(condtion)[vys_page.get_offset():vys_page.get_query_limit()]
        list_data = WisefinList()
        for x in obj:
            data_resp = PincodeResponse()
            data_resp.set_id(x.id)
            data_resp.set_no(x.no)
            data_resp.set_city_id(x.city_id)
            data_resp.set_district_id(x.district_id)
            list_data.append(data_resp)
        vpage = WisefinPaginator(obj, vys_page.get_index(), 10)
        list_data.set_pagination(vpage)
        return list_data


    def get_pincode(self,id):
        obj = Pincode.objects.get(id=id)
        data_resp = PincodeResponse()
        data_resp.set_id(obj.id)
        data_resp.set_no(obj.no)
        data_resp.set_city_id(obj.city_id)
        data_resp.set_district_id(obj.district_id)
        return data_resp

    def del_pincode(self, id):
        obj = Pincode.objects.filter(id=id).update(status=ActiveStatus.Delete)
        success_obj = Success()
        success_obj.set_status(SuccessStatus.SUCCESS)
        success_obj.set_message(SuccessMessage.DELETE_MESSAGE)
        return success_obj


#FOR PINCODE_DROPDOWN
    def get_pincode_add(self, id):
        obj = Pincode.objects.get(id=id)
        data_resp = PincodeResponse()
        data_resp.set_id(obj.id)
        data_resp.set_no(obj.no)
        return data_resp


    def fetch_pincode_search(self,query,vys_page):
        if query is None:
            pincodelist = Pincode.objects.filter(status=ActiveStatus.Active)

        else:
            pincodelist = Pincode.objects.filter(no__icontains=query, status=ActiveStatus.Active)

        list_data = WisefinList()
        for pincode in pincodelist:
            pincode_data = PincodeSearchResponse()
            pincode_data.set_id(pincode.id)
            pincode_data.set_district(pincode.district)
            pincode_data.set_city(pincode.city)
            pincode_data.set_newpi(pincode.no, pincode.city, pincode.district)
            list_data.append(pincode_data)
            vpage = WisefinPaginator(pincodelist, vys_page.get_index(), 10)
            list_data.set_pagination(vpage)
            return list_data

