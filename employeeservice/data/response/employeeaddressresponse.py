import json

from employeeservice.util.emputil import get_type_val
from masterservice.service.cityservice import CityService
from masterservice.service.districtservice import DistrictService
from masterservice.service.pincodeservice import PincodeService
from masterservice.service.stateservice import StateService


class EmployeeAddressResponse:
    id, line1, line2, line3, pincode_id, city_id, district_id, state_id, type = (None,) * 9


    def get(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)


    def set_id(self, id):
        self.id = id

    def set_line1(self, line1):
        self.line1 = line1

    def set_line2(self, line2):
        self.line2 = line2

    def set_line3(self, line3):
        self.line3 = line3

    def set_pincode_id(self, pincode_id):
        data_resp = PincodeService()
        pin_ser = data_resp.get_pincode_add(pincode_id)
        self.pincode_id = pin_ser

    def set_city_id(self, city_id):
        data_resp = CityService()
        city_serv = data_resp.get_city_add(city_id)
        self.city_id = city_serv

    def set_district_id(self, district_id):
        data_resp = DistrictService()
        dist_serv = data_resp.get_district_add(district_id)
        self.district_id = dist_serv

    def set_state_id(self, state_id):
        data_resp = StateService()
        state_serv = data_resp.get_state_add(state_id)
        self.state_id = state_serv

    def set_type(self, type):
        val = get_type_val(type)
        self.type = val