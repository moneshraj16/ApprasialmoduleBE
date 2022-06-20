from employeeservice.data.response.appraisalqueueresponse import AppraisalQueueResponse
from employeeservice.models import AppraisalQueue
from employeeservice.util.emputil import ActiveStatus
from utilityservice.data.response.emplist import WisefinList
from utilityservice.data.response.empmessage import WisefinMsg, SuccessMessage
from utilityservice.data.response.emppaginator import WisefinPaginator


class AppraisalQueueService:
    def appraisal_queue_create(self, data_obj):
        resp = WisefinMsg()
        if not data_obj.get_id() is None:
            obj = AppraisalQueue.objects.filter(id=data_obj.get_id()).update(appraisal_id=data_obj.get_appraisal_id(),
                                                                             from_user_id=data_obj.get_from_user_id(),
                                                                             to_user_id=data_obj.get_to_user_id(),
                                                                             comments=data_obj.get_comments())
            obj = AppraisalQueue.objects.get(id=data_obj.get_id())


        else:
            obj = AppraisalQueue.objects.create(id=data_obj.get_id(),
                                                appraisal_id=data_obj.get_appraisal_id(),
                                                from_user_id=data_obj.get_from_user_id(),
                                                to_user_id=data_obj.get_to_user_id(),
                                                comments=data_obj.get_comments())

            resp.set_message(SuccessMessage.CREATE_MESSAGE)

        return resp


    def fetch_appraisal_queue(self,vys_page):
        obj = AppraisalQueue.objects.filter(status=ActiveStatus.Active)
        list_data = WisefinList()
        for x in obj:
            data_resp = AppraisalQueueResponse()
            data_resp.set_id(x.id)
            data_resp.set_appraisal_id(x.appraisal_id)
            data_resp.set_from_user_id(x.from_user_id)
            data_resp.set_to_user_id(x.to_user_id)
            data_resp.set_comments(x.comments)
            list_data.append(data_resp)
        vpage = WisefinPaginator(obj, vys_page.get_index(), 10)
        list_data.set_pagination(vpage)
        return list_data