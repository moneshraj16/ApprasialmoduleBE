import json

from employeeservice.util.emputil import get_martial_status
from masterservice.service.countryservice import CountryService


class EmployeePersonalinfoResponse:
    id, martial_status, wedding_date, emc_contact_person, phone_regex, emc_contact_person_number, nationality = (None,) * 7

    def get(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

    def set_id(self, id):
        self.id = id

    def set_martial_status(self, martial_status):
        martial_info = get_martial_status(martial_status)
        self.martial_status = martial_info

    def set_wedding_date(self, wedding_date):
        self.wedding_date = str(wedding_date)

    def set_emc_contact_person(self, emc_contact_person):
        self.emc_contact_person = emc_contact_person

    def set_emc_contact_person_number(self, emc_contact_person_number):
        self.emc_contact_person_number = emc_contact_person_number

    def set_nationality(self, nationality):
        resp_serv = CountryService()
        val = resp_serv.get_country_info(nationality)
        self.nationality = val
