from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.db import models
from django.utils.timezone import now


class Employee (models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    code = models.CharField(max_length=24, unique=True, null=True)
    first_name = models.CharField(max_length=128, null=True, blank=True)
    middle_name = models.CharField(max_length=128, null=True, blank=True)
    last_name = models.CharField(max_length=128, null=True, blank=True)
    email_id = models.EmailField(null=True)
    designation = models.CharField(max_length=64, null=True, blank=True)
    doj = models.DateField(null=True, blank=True)
    # phone_regex = RegexValidator ( regex=r'^\?1?\d{9,15}$' ,
    #                                message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed." )
    # emc_contact_person_number = models.CharField ( validators=[ phone_regex ] , max_length=17 ,
    #                                                blank=True )
    gender = models.SmallIntegerField(default=-1, null=True, blank=True)
    dob = models.DateField(null=True, blank=True)
    department = models.SmallIntegerField(null=True)
    manager = models.CharField(max_length=128, null=True)
    employee_type = models.SmallIntegerField(default=1)
    grade = models.SmallIntegerField(default=1)
    status = models.SmallIntegerField(default=1)
    created_by = models.IntegerField(null=True, blank=True)
    created_date = models.DateTimeField(default=now)
    updated_by = models.IntegerField(null=True, blank=True)
    updated_date = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = "employeeservice_employee"


class EmployeeAddress (models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True)
    line1 = models.CharField(max_length=2048)
    line2 = models.CharField(max_length=2048, null=True, blank=True)
    line3 = models.CharField(max_length=2048, null=True, blank=True)
    type = models.SmallIntegerField(null=True)
    pincode_id = models.IntegerField(default=-1)
    city_id = models.IntegerField(default=-1)
    district_id = models.IntegerField(default=-1)
    state_id = models.IntegerField(default=-1)
    status = models.SmallIntegerField(default=1)
    created_by = models.IntegerField(null=True, blank=True)
    created_date = models.DateTimeField(default=now)
    updated_by = models.IntegerField(null=True, blank=True)
    updated_date = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = "employeeservice_employeeaddress"


class Employee_educationDetails(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True)
    inst_name = models.CharField(max_length=128,null=True)
    passing_year = models.IntegerField(null=True)
    percentage = models.FloatField(null=True)
    title = models.CharField(max_length=120)
    qualification = models.CharField(max_length=120)
    status = models.IntegerField(default=1)
    created_by = models.IntegerField(null=True)
    created_date = models.DateTimeField(default=now)
    updated_by = models.IntegerField(null=True, blank=True)
    updated_date = models.DateTimeField(null=True, blank=True)


class EmployeeExperiences(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True)
    company = models.CharField(max_length=240)
    work_experience = models.FloatField(null=True)
    period_from = models.DateField(null=True)
    period_to = models.DateField(null=True)
    role = models.CharField(max_length=120)
    city = models.CharField(max_length=120)
    status = models.IntegerField(default=1)
    created_by = models.IntegerField(null=True)
    created_date = models.DateTimeField(default=now)
    updated_by = models.IntegerField(null=True, blank=True)
    updated_date = models.DateTimeField(null=True, blank=True)


class EmployeePersionalInfo (models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True)
    martial_status = models.SmallIntegerField(null=True)
    wedding_date = models.DateField(null=True)
    emc_contact_person = models.CharField(max_length=120,null=True)
    phone_regex = RegexValidator(regex=r'^\?1?\d{9,10}$',
                                   message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    emc_contact_person_number = models.CharField(validators=[phone_regex], max_length=17,
                                      blank=True)
    nationality = models.SmallIntegerField(default=1)
    status = models.IntegerField(default=1)
    created_by = models.IntegerField(null=True)
    created_date = models.DateTimeField(default=now)
    updated_by = models.IntegerField(null=True, blank=True)
    updated_date = models.DateTimeField(null=True, blank=True)

class Employeedocuments(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True)
    file_path = models.FileField(null=True, upload_to='Employee_doc/')
    file_type = models.IntegerField(default=1)
    file_name = models.CharField(max_length=120, null=True)
    status = models.IntegerField(default=1)
    created_by = models.IntegerField(null=True)
    created_date = models.DateTimeField(default=now)
    updated_by = models.IntegerField(null=True, blank=True)
    updated_date = models.DateTimeField(null=True, blank=True)


class Appraisal(models.Model):
    employee = models.IntegerField(default=1)
    designation = models.CharField(max_length=64, null=True, blank=True)
    appraisal_status = models.IntegerField(default=1)
    grade = models.SmallIntegerField(default=1)
    status = models.IntegerField(default=1)
    created_by = models.IntegerField(null=True)
    created_date = models.DateTimeField(default=now)
    updated_by = models.IntegerField(null=True, blank=True)
    updated_date = models.DateTimeField(null=True, blank=True)


class Appraisaldetails(models.Model):
    appraisal = models.ForeignKey(Appraisal, on_delete=models.SET_NULL, null=True)
    remarks = models.TextField(max_length=125, null=True)
    rating = models.IntegerField(null=True, blank=True)
    status = models.IntegerField(default=1)
    created_by = models.IntegerField(null=True)
    created_date = models.DateTimeField(default=now)
    updated_by = models.IntegerField(null=True, blank=True)
    updated_date = models.DateTimeField(null=True, blank=True)



class AppraisalQueue(models.Model):
    appraisal = models.ForeignKey(Appraisal, on_delete=models.SET_NULL, null=True)
    from_user_id = models.IntegerField(null=False)
    to_user_id = models.IntegerField(null=False)
    created_date = models.DateTimeField(default=now)
    comments = models.CharField(null=False, max_length=2048)
    status = models.SmallIntegerField(default=1)
    is_sys = models.BooleanField(default=False)