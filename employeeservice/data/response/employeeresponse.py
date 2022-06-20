import json

from employeeservice.util.emputil import employee_type_val, gender_type_val, grade_type_val
from masterservice.service.departementservice import DepartmentService
from masterservice.service.designationservice import DesignationService


class EmployeeResponse:
    id, user_id, code, first_name, middle_name, last_name, email_id, designation, doj, gender, dob, department, manager, employee_type, grade = (None,)*15

    def get(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

    def set_id(self, id):
        self.id = id

    def set_user_id(self, user_id):
        self.user_id = user_id

    def set_code(self, code):
        self.code = code

    def set_first_name(self, first_name):
        self.first_name = first_name

    def set_middle_name(self, middle_name):
        self.middle_name = middle_name

    def set_last_name(self, last_name):
        self.last_name = last_name

    def set_email_id(self, email_id):
        self.email_id = email_id

    def set_designation(self, designation):
        res_serv = DesignationService()
        val = res_serv.get_designation_info(designation)
        self.designation = val

    def set_doj(self, doj):
        self.doj = str(doj)

    def set_gender(self, gender):
        vals = gender_type_val(gender)
        self.gender = vals

    def set_dob(self, dob):
        self.dob = str(dob)

    def set_department(self, department):
        data_serv = DepartmentService()
        dep_sis = data_serv.get_departments(department)
        self.department = dep_sis

    def set_manager(self, manager):
        self.manager = manager

    def set_employee_type(self, employee_type):
        val = employee_type_val(employee_type)
        self.employee_type = val

    def set_grade(self, grade):
        vals = grade_type_val(grade)
        self.grade = vals
