from employeeservice.data.response.appraisaldetailresponse import AppraisalDetailResponse
from employeeservice.models import Appraisaldetails
from employeeservice.util.emputil import ActiveStatus
from utilityservice.data.response.emplist import WisefinList
from utilityservice.data.response.empmessage import WisefinMsg, SuccessMessage, Success, SuccessStatus
from utilityservice.data.response.emppaginator import WisefinPaginator


class AppraisalDetailService:
    def appraisal_detail_create(self, data_obj, appraisal_id):
        resp = WisefinMsg()
        if not data_obj.get_id() is None:
            obj = Appraisaldetails.objects.filter(id=data_obj.get_id()).update(appraisal_id=appraisal_id,
                                                                               remarks=data_obj.get_remarks(),
                                                                               rating=data_obj.get_rating())

            obj = Appraisaldetails.objects.get(id=data_obj.get_id())


        else:
            obj = Appraisaldetails.objects.create(id=data_obj.get_id(), appraisal_id=appraisal_id,
                                                  remarks=data_obj.get_remarks(),
                                                  rating=data_obj.get_rating())

            resp.set_message(SuccessMessage.CREATE_MESSAGE)

        return resp


    def fetch_appraisal_detail(self,vys_page):
        obj = Appraisaldetails.objects.filter(status=ActiveStatus.Active)
        list_data = WisefinList()
        for x in obj:
            data_resp = AppraisalDetailResponse()
            data_resp.set_id(x.id)
            data_resp.set_appraisal_id(x.appraisal_id)
            data_resp.set_rating(x.rating)
            data_resp.set_remarks(x.remarks)
            list_data.append(data_resp)
        vpage = WisefinPaginator(obj, vys_page.get_index(), 10)
        list_data.set_pagination(vpage)
        return list_data

    def get_appraisal_detail(self, id):
        obj = Appraisaldetails.objects.get(id=id)
        data_resp = AppraisalDetailResponse()
        data_resp.set_id(obj.id)
        data_resp.set_appraisal_id(obj.appraisal_id)
        data_resp.set_rating(obj.rating)
        data_resp.set_remarks(obj.remarks)
        return data_resp

    def del_appraisal_detail(self,id):
        obj = Appraisaldetails.objects.filter(id=id).update(status=ActiveStatus.Delete)
        success_obj = Success()
        success_obj.set_status(SuccessStatus.SUCCESS)
        success_obj.set_message(SuccessMessage.DELETE_MESSAGE)
        return success_obj


#FOR OVERALL_GET
    def get_appraisal_details(self, appraisal_id):
        details_obj = Appraisaldetails.objects.filter(status=ActiveStatus.Active, appraisal_id=appraisal_id)
        list_data = []
        for obj in details_obj:
            data_resp = AppraisalDetailResponse()
            data_resp.set_id(obj.id)
            data_resp.set_rating(obj.rating)
            data_resp.set_remarks(obj.remarks)
            data_resp.set_appraisal_id(obj.appraisal_id)
            list_data.append(data_resp)

        return list_data

