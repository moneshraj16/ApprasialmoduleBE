from django.db.models import Q

from masterservice.data.response.departementresponse import DepartementResponse
from masterservice.models.mastermodels import Department
from masterservice.util.masterutil import DepartmentrefType
from utilityservice.data.response.empmessage import WisefinMsg
from utilityservice.data.response.empmessage import WisefinMsg, SuccessMessage, ErrorMessage, Success, SuccessStatus, Error, ErrorDescription
from utilityservice.data.response.emplist import WisefinList
from employeeservice.util.emputil import ActiveStatus
from utilityservice.data.response.emppaginator import WisefinPaginator



class DepartmentService:
    def create_department(self, data_obj, dep_id):
        resp = WisefinMsg()
        if not dep_id is None:
            Department.objects.filter(id=dep_id).update(**data_obj)
            resp.set_message(SuccessMessage.UPDATE_MESSAGE)

        else:
            obj = Department.objects.create(**data_obj)
            obj.code = DepartmentrefType.DEPT + str(obj.id)
            obj.save()
            resp.set_message(SuccessMessage.CREATE_MESSAGE)
        return resp

    def fetch_department(self, vys_page, request):
        query = request.GET.get('query')
        condtion = Q(status=ActiveStatus.Active)
        if query is not None and query != '':
            condtion &= (Q(name__icontains=query)) | (Q(code__icontains=query))
        dep_obj = Department.objects.filter(condtion)[vys_page.get_offset():vys_page.get_query_limit()]
        list_data = WisefinList()
        for obj in dep_obj:
            data_resp = DepartementResponse()
            data_resp.set_id(obj.id)
            data_resp.set_name(obj.name)
            data_resp.set_description(obj.description)
            data_resp.set_code(obj.code)
            list_data.append(data_resp)
        vpage = WisefinPaginator(dep_obj, vys_page.get_index(), 10)
        list_data.set_pagination(vpage)
        return list_data

    def get_department(self, id):
        dep_obj = Department.objects.get(id=id)
        data_resp = DepartementResponse()
        data_resp.set_id(dep_obj.id)
        data_resp.set_name(dep_obj.name)
        data_resp.set_description(dep_obj.description)

        return data_resp

    def del_department(self,id):
        Department.objects.filter(id=id).update(status=ActiveStatus.Delete)
        success_obj = Success()
        success_obj.set_status(SuccessStatus.SUCCESS)
        success_obj.set_message(SuccessMessage.DELETE_MESSAGE)

        return success_obj

#FOR EMPLOYEE_DEP_DROPDOWN
    def get_departments(self, id):
        obj = Department.objects.get(id=id)
        data_resp = DepartementResponse()
        data_resp.set_id(obj.id)
        data_resp.set_name(obj.name)
        data_resp.set_code(obj.code)
        return data_resp

