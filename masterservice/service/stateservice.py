from django.db.models import Q

from employeeservice.util.emputil import ActiveStatus
from masterservice.data.response.stateresponse import StateResponse
from masterservice.util.masterutil import MasterrefType
from utilityservice.data.response.emplist import WisefinList
from utilityservice.data.response.empmessage import WisefinMsg, SuccessMessage, Success, SuccessStatus
from masterservice.models.mastermodels import State
from utilityservice.data.response.emppaginator import WisefinPaginator


class StateService:
    def create_state(self, state_id, data_obj):
        resp = WisefinMsg()

        if not state_id is None:
            State.objects.filter(id=state_id).update(**data_obj)
            resp.set_message(SuccessMessage.UPDATE_MESSAGE)


        else:
            obj = State.objects.create(**data_obj)
            obj.code = MasterrefType.STATE + str(obj.id)
            obj.save()
            resp.set_message(SuccessMessage.CREATE_MESSAGE)
            resp.name = obj.name
            resp.code = obj.code

        return resp

    def fetch_state(self, vys_page, request):
        query = request.GET.get('query')
        condtion = Q(status=ActiveStatus.Active)
        if query is not None and query != '':
            condtion &= Q(name__icontains=query)
        obj = State.objects.filter(condtion)[vys_page.get_offset():vys_page.get_query_limit()]
        list_data = WisefinList()
        for x in obj:
            data_resp = StateResponse()
            data_resp.set_id(x.id)
            data_resp.set_name(x.name)
            data_resp.set_code(x.code)
            data_resp.set_country_id(x.country_id)
            list_data.append(data_resp)
        vpage = WisefinPaginator(obj, vys_page.get_index(), 10)
        list_data.set_pagination(vpage)
        return list_data

    def get_state(self, id):
        obj = State.objects.get(id=id)
        data_resp = StateResponse()
        data_resp.set_id(obj.id)
        data_resp.set_name(obj.name)
        data_resp.set_code(obj.code)
        data_resp.set_country_id(obj.country_id)
        return data_resp

    def del_state(self, id):
        obj = State.objects.filter(id=id).update(status=ActiveStatus.Delete)
        success_obj = Success()
        success_obj.set_status(SuccessStatus.SUCCESS)
        success_obj.set_message(SuccessMessage.DELETE_MESSAGE)

        return success_obj

#FOR STATE DROPDOWN
    def get_state_add(self, id):
        obj = State.objects.get(id=id)
        data_resp = StateResponse()
        data_resp.set_id(obj.id)
        data_resp.set_name(obj.name)
        data_resp.set_code(obj.code)
        return data_resp
