from django.db.models import Q

from employeeservice.util.emputil import ActiveStatus
from masterservice.data.response.countryresponse import CountryResponse
from masterservice.models import Country
from masterservice.util.masterutil import MasterrefType
from utilityservice.data.response.emplist import WisefinList
from utilityservice.data.response.empmessage import WisefinMsg, SuccessMessage, Success, SuccessStatus
from utilityservice.data.response.emppaginator import WisefinPaginator


class CountryService:
    def create_country(self, country_id, data_obj):
        resp = WisefinMsg()
        if not country_id is None:
            Country.objects.filter(id=country_id).update(**data_obj)
            resp.set_message(SuccessMessage.UPDATE_MESSAGE)

        else:
            obj = Country.objects.create(**data_obj)
            obj.code = MasterrefType.COUNTRY + str(obj.id)
            obj.save()
            resp.set_message(SuccessMessage.CREATE_MESSAGE)
            resp.code = obj.code
            resp.name = obj.name

        return resp

    def fetch_country(self, vys_page, request):
        query = request.GET.get('query')
        condtion = Q(status=ActiveStatus.Active)
        if query is not None and query != '':
            condtion &= (Q(name__icontains=query))
        obj = Country.objects.filter(condtion)[vys_page.get_offset():vys_page.get_query_limit()]
        list_data = WisefinList()
        for x in obj:
            data_resp = CountryResponse()
            data_resp.set_id(x.id)
            data_resp.set_name(x.name)
            data_resp.set_code(x.code)
            list_data.append(data_resp)
        vpage = WisefinPaginator(obj, vys_page.get_index(), 10)
        list_data.set_pagination(vpage)
        return list_data

    def get_country(self,id):
        obj = Country.objects.get(id=id)
        data_resp = CountryResponse()
        data_resp.set_id(obj.id)
        data_resp.set_name(obj.name)
        data_resp.set_code(obj.code)
        return data_resp

    def del_country(self, id):
        obj = Country.objects.filter(id=id).update(status=ActiveStatus.Active)
        success_obj = Success()
        success_obj.set_status(SuccessStatus.SUCCESS)
        success_obj.set_message(SuccessMessage.DELETE_MESSAGE)
        return success_obj

#FOR_EMPLOYEE_DROPDOWN

    def get_country_info(self,id):
        obj = Country.objects.get(id=id)
        data_resp = CountryResponse()
        data_resp.set_id(obj.id)
        data_resp.set_code(obj.code)
        data_resp.set_name(obj.name)
        return data_resp