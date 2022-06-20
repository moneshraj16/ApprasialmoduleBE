import json

from employeeservice.service.employeeservice import EmployeeService
from employeeservice.util.emputil import grade_type_val, Appraisal_type_val
from masterservice.service.designationservice import DesignationService


class AppraisalResponse:
    id, employee, designation, appraisal_status, grade = (None,) * 5

    def get(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

    def set_id(self, id):
        self.id = id

    def set_employee(self, employee):
        emp_serv = EmployeeService()
        val = emp_serv.employee_get_info(employee)
        self.employee = val

    def set_designation(self, designation):
        desg_serv = DesignationService()
        val = desg_serv.get_designation_info(designation)
        self.designation = val

    def set_appraisal_status(self, appraisal_status):
        val = Appraisal_type_val(appraisal_status)
        self.appraisal_status = val

    def set_grade(self, grade):
        val = grade_type_val(grade)
        self.grade = val

