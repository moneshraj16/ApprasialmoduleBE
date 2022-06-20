from django.db.models import Q

from employeeservice.data.response.appraisalresponse import AppraisalResponse
from employeeservice.models import Appraisal, AppraisalQueue
from employeeservice.util.emputil import ActiveStatus
from utilityservice.data.response.emplist import WisefinList
from utilityservice.data.response.empmessage import SuccessMessage, WisefinMsg, Success, SuccessStatus
from utilityservice.data.response.emppaginator import WisefinPaginator


class AppraisalService:
    def appraisal_create(self, data_obj):
        resp = WisefinMsg()
        if not data_obj.get_id() is None:
            appraisal = Appraisal.objects.filter(id=data_obj.get_id()).update(employee=data_obj.get_employee(),
                                                                        designation=data_obj.get_designation(),
                                                                        appraisal_status=data_obj.get_appraisal_status(),
                                                                        grade=data_obj.get_grade())

            appraisal = Appraisal.objects.get(id=data_obj.get_id())


        else:
            appraisal = Appraisal.objects.create(id=data_obj.get_id(),
                                           designation=data_obj.get_designation(),
                                           appraisal_status=data_obj.get_appraisal_status(),
                                           grade=data_obj.get_grade())

            appraisal = AppraisalQueue.objects.create(appraisal_id=appraisal.id, from_user_id='1', to_user_id='1', comments='')
            # resp.set_message(SuccessMessage.CREATE_MESSAGE)

        return appraisal.id

    def fetch_appraisal(self, vys_page,request):
        query = request.GET.get('query')
        condtion = Q(status=ActiveStatus.Active)
        if query is not None and query != '':
            condtion &= Q(employee=query)
        obj = Appraisal.objects.filter(condtion)
        list_data = WisefinList()
        for x in obj:
            data_resp = AppraisalResponse()
            data_resp.set_id(x.id)
            data_resp.set_employee(x.employee)
            data_resp.set_designation(x.designation)
            data_resp.set_appraisal_status(x.appraisal_status)
            data_resp.set_grade(x.grade)
            list_data.append(data_resp)
        vpage = WisefinPaginator(obj, vys_page.get_index(), 10)
        list_data.set_pagination(vpage)
        return list_data

    def get_appraisal(self, id):
        obj = Appraisal.objects.get(id=id)
        data_resp = AppraisalResponse()
        data_resp.set_id(obj.id)
        data_resp.set_grade(obj.grade)
        data_resp.set_designation(obj.designation)
        data_resp.set_appraisal_status(obj.appraisal_status)
        data_resp.set_employee(obj.employee)
        return data_resp

    def del_appraisal(self, id):
        obj = Appraisal.objects.filter(id=id).update(status=ActiveStatus.Delete)
        success_obj = Success()
        success_obj.set_status(SuccessStatus.SUCCESS)
        success_obj.set_message(SuccessMessage.DELETE_MESSAGE)
        return success_obj