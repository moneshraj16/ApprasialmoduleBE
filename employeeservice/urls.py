from django.conf import settings
from django.urls import path

from django.conf.urls.static import static


from employeeservice.controller import employeecontroller, usercontroller, appraisalcontroller

urlpatterns = [
    # path('signup', employeecontroller.create_user, name='create_user'),
    # path('auth_token', employeecontroller.auth_token, name='auth_token'),
    path('employee', employeecontroller.create_employee, name='employee'),
    path('employee/<id>', employeecontroller.get_employee, name='employee'),
    path('employee/<employee_id>/employee_addr', employeecontroller.create_employee_addr, name='employee_addr'),
    path('employee_addr/<id>', employeecontroller.get_employee_addr, name='employee'),
    path('employee/<employee_id>/employee_edu', employeecontroller.create_employee_edu, name='employee_edu'),
    path('employee_edu/<id>', employeecontroller.get_employee_edu, name='employee_edu'),
    path('employee/<employee_id>/employee_exp', employeecontroller.create_employee_exp, name='employee_exp'),
    path('employee_exp/<id>', employeecontroller.get_employee_exp, name='employee_exp'),
    path('employee/<employee_id>/employee_personlinfo', employeecontroller.create_emp_personalinfo, name= 'employee_per_info'),
    path('employee_personinfo/<id>', employeecontroller.get_employee_perinfo, name='employeee_per_info'),
    #employee_doc_attachment and view_file
    path('employee/<employee_id>/employee_doc', employeecontroller.create_employee_doc, name='employee_doc'),
    path('view_attachment/<file_id>', employeecontroller.emp_view_file, name='view_attachment'),
    path('emp_file_get/<employee_id>', employeecontroller.emp_file_get, name='emp_file'),
    path('employee_doc/<employee_id>', employeecontroller.get_employee_doc, name='employee_doc'),
    path('employee_doc_del/<id>', employeecontroller.del_emloyee_doc, name='employee_doc'),
    #doc_attachment_download
    path('employee_file_downlode/<file_id>', employeecontroller.employee_file_download, name='employee_file_downlode'),
    #employee_information
    path('employee/<employee_id>/employee_get', employeecontroller.employee_get, name='employee_get'),
    #employee_employee_type_dropdown
    path('employee_type', employeecontroller.get_employee_dropdown, name='employee_type'),
    path('employee_type_get/<type_id>', employeecontroller.employee_type_get, name='employee_type_get'),
    #grade_dropdown
    path('grade/<id>', employeecontroller.get_grade, name='grade'),
    path('grade', employeecontroller.fetch_grade, name='grade'),
    #SIGNUP AND LOGIN
    path('signup', usercontroller.create_user, name='signup'),
    path('login', employeecontroller.auth_token, name='auth_token'),

    #APPRAISAL_CREATE

    path('appraisal_create', appraisalcontroller.appraisal_create, name='appraisal'),
    path('get_appraisal/<id>', appraisalcontroller.get_appraisal, name='appraisal'),
    #appraisal_detail_create
    path('appraisal_detail_create', appraisalcontroller.appraisal_detail_create, name='appraisal_detail'),
    path('get_appraisal_detail/<id>', appraisalcontroller.get_appraisal_details, name='appraisal_detail'),
    #appraisal_queue_create
    path('appraisal_queue_create', appraisalcontroller.appraisal_queue_create, name='appraisal_queue'),
    #appraisal_get
    path('appraisal_create/<appraisal_id>/appraisal_get', appraisalcontroller.appraisal_get,name='appraisal_get'),
              ]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)