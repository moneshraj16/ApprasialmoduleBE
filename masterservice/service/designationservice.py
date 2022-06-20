from django.db.models import Q

from employeeservice.util.emputil import ActiveStatus
from masterservice.data.response.designationresponse import DesignationResponse
from masterservice.models import Designation
from masterservice.util.masterutil import MasterrefType
from utilityservice.data.response.emplist import WisefinList
from utilityservice.data.response.empmessage import WisefinMsg, SuccessMessage, Success, SuccessStatus
from utilityservice.data.response.emppaginator import WisefinPaginator


class DesignationService:
    def create_designation(self, designation_id, data_obj):
        resp = WisefinMsg()
        if not designation_id is None:
            Designation.objects.filter(id=designation_id).update(**data_obj)
            resp.set_message(SuccessMessage.UPDATE_MESSAGE)

        else:
            obj = Designation.objects.create(**data_obj)
            obj.code = MasterrefType.DESIG + str(obj.id)
            obj.save()
            resp.set_message(SuccessMessage.CREATE_MESSAGE)
        return resp


    def fetch_designation(self,vys_page, request):
        query = request.GET.get('query')
        condtion = Q(status=ActiveStatus.Active)
        if query is not None and query != '':
            condtion &= (Q(name__icontains=query))
        desig_obj = Designation.objects.filter(condtion)[vys_page.get_offset():vys_page.get_query_limit()]
        list_data = WisefinList()
        for obj in desig_obj:
            data_resp = DesignationResponse()
            data_resp.set_id(obj.id)
            data_resp.set_name(obj.name)
            data_resp.set_code(obj.code)
            list_data.append(data_resp)
        vpage = WisefinPaginator(desig_obj, vys_page.get_index(), 10)
        list_data.set_pagination(vpage)
        return list_data


    def get_designation(self,id):
        obj = Designation.objects.get(id=id)
        data_resp = DesignationResponse()
        data_resp.set_id(obj.id)
        data_resp.set_code(obj.code)
        data_resp.set_name(obj.name)

        return data_resp


    def del_designation(self, id):
        Designation.objects.filter(id=id).update(status=ActiveStatus.Delete)
        success_obj = Success()
        success_obj.set_status(SuccessStatus.SUCCESS)
        success_obj.set_message(SuccessMessage.DELETE_MESSAGE)

        return success_obj

#FOR_EMPLOYEE_DROPDOWN

    def get_designation_info(self,id):
        obj =Designation.objects.get(id=id)
        data_resp = DesignationResponse()
        data_resp.set_id(obj.id)
        data_resp.set_code(obj.code)
        data_resp.set_name(obj.name)

        return data_resp