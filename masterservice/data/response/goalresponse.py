import json

from employeeservice.util.emputil import grade_type_val
from masterservice.service.designationservice import DesignationService


class GoalResponse:
    id, goal, description, grade, designation_id,name = (None,)*6

    def get(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)

    def set_id(self, id):
        self.id = id

    def set_goal(self, goal):
        self.goal = goal

    def set_description(self, description):
        self.description = description

    def set_grade(self, grade):
        val = grade_type_val(grade)
        self.grade = val

    def set_designation(self, designation_id):
        resp_obj = DesignationService()
        val = resp_obj.get_designation_info(designation_id)
        self.designation_id = val

    def set_name(self, name):
        self.name = name