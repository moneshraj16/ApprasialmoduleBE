from django.db.models import Q

from employeeservice.util.emputil import ActiveStatus
from masterservice.data.response.goalresponse import GoalResponse
from masterservice.models import Goal, Designation
from utilityservice.data.response.emplist import WisefinList
from utilityservice.data.response.empmessage import WisefinMsg, SuccessMessage, Success, SuccessStatus
from utilityservice.data.response.emppaginator import WisefinPaginator


class GoalService:
    def create_goal(self, data_obj, goal_id):
        resp = WisefinMsg()
        if goal_id is not None:
            Goal.objects.filter(id=goal_id).update(**data_obj)
            resp.set_message(SuccessMessage.UPDATE_MESSAGE)

        else:
            Goal.objects.create(**data_obj)
            resp.set_message(SuccessMessage.CREATE_MESSAGE)

        return resp

    def fetch_goal(self, vys_page, request):
        query = request.GET.get('query')
        # grade = request.GET.get('grade')
        condtion = Q(status=ActiveStatus.Active)
        if query is not None and query !='':
            condtion &= Q(name__icontains=query)
        # if grade is not None and grade != '':
        #     condtion &= Q(grade=grade)
        # if query is not None and query != '':
        #     designation = Designation.objects.filter(name__icontains=query).values_list('id', flat=True)
        #     designation = list(designation)
        #     condtion &= Q(goal__icontains=query) | Q(designation_id__in=designation)
        goal_obj = Goal.objects.filter(condtion)
        list_data = WisefinList()
        for obj in goal_obj:
            data_resp = GoalResponse()
            data_resp.set_id(obj.id)
            data_resp.set_name(obj.name)
            # data_resp.set_goal(obj.goal)
            data_resp.set_description(obj.description)
            # data_resp.set_grade(obj.grade)
            # data_resp.set_designation(obj.designation.id)
            list_data.append(data_resp)
        vpage = WisefinPaginator(goal_obj, vys_page.get_index(), 10)
        list_data.set_pagination(vpage)
        return list_data

    def get_goal(self, id):
        obj = Goal.objects.get(id=id)
        data_resp = GoalResponse()
        data_resp.set_id(obj.id)
        data_resp.set_name(obj.name)
        # data_resp.set_goal(obj.goal)
        # data_resp.set_description(obj.description)

        return data_resp

    def del_goal(self, id):
        obj = Goal.objects.filter(id=id).update(status=ActiveStatus.Delete)
        success_obj = Success()
        success_obj.set_message(SuccessMessage.DELETE_MESSAGE)
        success_obj.set_status(SuccessStatus.SUCCESS)
        return success_obj

#FOR EDIT SCREEN

    def goal_get(self, id):
        obj = Goal.objects.get(id=id)
        data_resp = GoalResponse()
        data_resp.set_id(obj.id)
        data_resp.set_name(obj.name)
        data_resp.set_description(obj.description)
        return data_resp

