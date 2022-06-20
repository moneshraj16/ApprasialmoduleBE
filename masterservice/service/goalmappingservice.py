from django.db.models import Q

from employeeservice.util.emputil import ActiveStatus
from masterservice.data.response.goalmappingresponse import GoalMappingResponse
from masterservice.data.response.goalresponse import GoalResponse
from utilityservice.data.response.emplist import WisefinList
from utilityservice.data.response.empmessage import WisefinMsg, SuccessMessage, Success, SuccessStatus
from masterservice.models.mastermodels import GoalMapping
from utilityservice.data.response.emppaginator import WisefinPaginator


class GoalMappingService:
    def create_goal_mapping(self, data_obj, sub_goal):
        resp = WisefinMsg()
        if not data_obj.get_id() is None:
            GoalMapping.objects.filter(id=data_obj.get_id()).update(sub_goal=sub_goal,
                                                                    grade=data_obj.get_grade(),
                                                                    designation_id=data_obj.get_designation_id(),
                                                                    goal_id=data_obj.get_goal_id())

            obj = GoalMapping.objects.get(id=data_obj.get_id())

        else:
            obj = GoalMapping.objects.create(id=data_obj.get_id(),
                                             sub_goal=sub_goal,
                                             grade=data_obj.get_grade(),
                                             designation_id=data_obj.get_designation_id(),
                                             goal_id=data_obj.get_goal_id())



            resp.set_message(SuccessMessage.CREATE_MESSAGE)


        return resp

    def fetch_goal_mapping(self, vys_page, request):
        # query = request.GET.get('query')
        grade = request.GET.get('grade')
        designation = request.GET.get('designation')
        condtion = Q(status=ActiveStatus.Active)
        # if query is not None and query != '':
        #     condtion &= Q(sub_goal__icontains=query)
        if grade is not None and grade != '':
            condtion &= Q(grade=grade)
        if designation is not None and designation != '':
            condtion &= Q(designation_id__in=designation)
        goal_obj = GoalMapping.objects.filter(condtion)[vys_page.get_offset():vys_page.get_query_limit()]
        list_data = WisefinList()
        for obj in goal_obj:
            data_resp = GoalMappingResponse()
            data_resp.set_id(obj.id)
            data_resp.set_sub_goal(obj.sub_goal)
            data_resp.set_grade(obj.grade)
            data_resp.set_designation_id(obj.designation_id)
            data_resp.set_goal_id(obj.goal.id)
            list_data.append(data_resp)
        vpage = WisefinPaginator(goal_obj, vys_page.get_index(), 10)
        list_data.set_pagination(vpage)
        return list_data


    def get_goal_mapping(self, id):
        obj = GoalMapping.objects.get(id=id)
        data_resp = GoalMappingResponse()
        data_resp.set_id(obj.id)
        data_resp.set_sub_goal(obj.sub_goal)
        data_resp.set_goal_id(obj.goal_id)
        data_resp.set_grade(obj.grade)
        data_resp.set_designation_id(obj.designation_id)

        return data_resp


    def del_goal_mapping(self,id):
        GoalMapping.objects.filter(id=id).update(status=ActiveStatus.Delete)
        success_obj = Success()
        success_obj.set_status(SuccessStatus.SUCCESS)
        success_obj.set_message(SuccessMessage.DELETE_MESSAGE)

        return success_obj

