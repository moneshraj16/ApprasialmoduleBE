from datetime import datetime
from sys import prefix

from django.http import HttpResponse

from utilityservice.data.response.empmessage import WisefinMsg, SuccessMessage, ErrorMessage, Success, SuccessStatus, Error, ErrorDescription
from utilityservice.data.response.emplist import WisefinList
from employeeservice.util.emputil import ActiveStatus
from utilityservice.data.response.emppaginator import WisefinPaginator
from employeeservice.models.employeemodels import Employeedocuments
from employeeservice.data.response.employeedocumentresponse import EmployeeDocumentResponse
from employeeservice.util.emputil import document_upload


class EmployeeDocumentService:
    def create_empdocument(self, request, employee_id):
        resp = WisefinMsg()
        if not request.FILES['file1'] is None:
            try:
                file_count = len(request.FILES.getlist('file1'))
                file_type = document_upload.file1
                # file_path = files['file_path']
                for i in range(0, file_count):
                    file = request.FILES.getlist('file1')[i]
                    file_name = file.name
                    file_size = file.size
                    file_name_new = 'DOC' + str(datetime.now().strftime("%y%m%d_%H%M%S")) + file_name
                    print(file_name_new)
                    obj = Employeedocuments.objects.create(file_path=file,
                                                           file_type=file_type,
                                                           file_name=file_name, employee_id=employee_id)


            except KeyError:
                print('Kindly pass file information')

        if not request.FILES['file2'] is None:
            try:
                file_count = len(request.FILES.getlist('file2'))
                file_type = document_upload.file2
                # file_path = files['file_path']
                for i in range(0, file_count):
                    file = request.FILES.getlist('file2')[i]
                    file_name = file.name
                    file_size = file.size
                    file_name_new = 'DOC' + str(datetime.now().strftime("%y%m%d_%H%M%S")) + file_name
                    print(file_name_new)
                    obj = Employeedocuments.objects.create(file_path=file,
                                                           file_type=file_type,
                                                           file_name=file_name, employee_id=employee_id)

            except KeyError:
                print('Kindly pass file information')
        resp.set_message(SuccessMessage.CREATE_MESSAGE)
        return resp


            # Employeedocuments.objects.filter(id=data_obj.get_id()).update(file_path=data_obj['file_path'],
            #                                                               file_type=data_obj['file_type'],
            #                                                               file_name=file)
            # obj = Employeedocuments.objects.get(id=data_obj.get_id())

        # else:

    def fetch_empdoument(self, vys_page, employee_id):
        empdoc_obj = Employeedocuments.objects.filter(status=ActiveStatus.Active, employee_id=employee_id)
        list_data = WisefinList()
        for obj in empdoc_obj:
            data_resp = EmployeeDocumentResponse()
            data_resp.set_id(obj.id)
            data_resp.set_file_path(obj.path)
            data_resp.set_file_name(obj.file_name)
            data_resp.set_file_type(obj.file_type)
            data_resp.set_status(obj.status)
            list_data.append(data_resp)
        vpage = WisefinPaginator(empdoc_obj, vys_page.get_index(), 10)
        list_data.set_pagination(vpage)
        return list_data

#EDIT_EMPLOYEE_DOCUMENT
    def create_empdocuments(self,  request, employee_id):
        resp = WisefinMsg()
        try:
            if not request.FILES['file1'] is None:
                try:
                    file_count = len(request.FILES.getlist('file1'))
                    file_type = document_upload.file1
                    # file_path = files['file_path']
                    for i in range(0, file_count):
                        file = request.FILES.getlist('file1')[i]
                        file_name = file.name
                        file_size = file.size
                        file_name_new = 'DOC' + str(datetime.now().strftime("%y%m%d_%H%M%S")) + file_name
                        print(file_name_new)
                        obj = Employeedocuments.objects.create(file_path=file,
                                                               file_type=file_type,
                                                               file_name=file_name, employee_id=employee_id)


                except KeyError:
                    print('Kindly pass file information')
        except:
            pass
        try:
            if not request.FILES['file2'] is None:
                try:
                    file_count = len(request.FILES.getlist('file2'))
                    file_type = document_upload.file2
                    # file_path = files['file_path']
                    for i in range(0, file_count):
                        file = request.FILES.getlist('file2')[i]
                        file_name = file.name
                        file_size = file.size
                        file_name_new = 'DOC' + str(datetime.now().strftime("%y%m%d_%H%M%S")) + file_name
                        print(file_name_new)
                        obj = Employeedocuments.objects.create(file_path=file,
                                                               file_type=file_type,
                                                               file_name=file_name, employee_id=employee_id)

                except KeyError:
                    print('Kindly pass file information')
        except:
            pass
        resp.set_message(SuccessMessage.CREATE_MESSAGE)
        return resp

#DELETE_EMPLOYEE_DOCUMENT
    def del_empdocument(self, id):
        try:
            obj = Employeedocuments.objects.filter(id=id).delete()
            resp = Success()
            resp.set_status(SuccessStatus.SUCCESS)
            resp.set_message(SuccessMessage.DELETE_MESSAGE)
        except:
            resp = Error()
            resp.set_description(ErrorDescription.INVALID_DATA)
            resp.set_code('400')
        return resp

#EMPLOYEE_FILE_VIEW
    def file_view(self, file_id):
        doc_id = file_id
        # obj_id = doc_id.split('_')[-1]
        doc_obj = Employeedocuments.objects.get(id=doc_id)
        file = doc_obj.file_path
        file_name = doc_obj.file_name
        contentType = file_name.split('.')[-1]
        response = HttpResponse(file)
        response['Content-Disposition'] = 'attachments; filename="{}"'.format(file_name)
        return response


    def get_document(self, employee_id):
        doc_obj = Employeedocuments.objects.filter(employee_id=employee_id)
        arr = []
        for obj in doc_obj:
            data_resp = EmployeeDocumentResponse()
            data_resp.file_name(obj.file_name)
            data_resp.set_id(obj.id)
            arr.append(data_resp)
        return arr
        #     value = {}
        #     value['file_name'] = obj.file_name
        #     value['id'] = obj.id
        #     arr.append(value)
        # return arr



#EMPLOYEE_FILE_DOWNLOAD
    def employee_file_downlode(self, file_id):
        doc_id = file_id
        obj_id = doc_id.split('_')[-1]
        doc_obj = Employeedocuments.objects.get(id=obj_id)
        print(type(doc_obj))
        file = doc_obj.file_path
        file_name = doc_obj.file_name
        # contentType = file_name.split('.')[-1]
        response = HttpResponse(file)
        response['Content-Disposition'] = 'attachments; filename="{}"'.format(file_name)
        return response