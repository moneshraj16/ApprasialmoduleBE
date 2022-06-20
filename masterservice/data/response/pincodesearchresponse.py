import json

from masterservice.data.response.cityresponse import CityResponse
from masterservice.data.response.districtresponse import DistrictResponse
from masterservice.data.response.stateresponse import StateResponse


class PincodeSearchResponse:
    id, district, city, newpi, no, state = (None,) *6

    def get(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)

    def set_id(self, id):
        self.id = id

    def set_district(self, district):
        district_data = DistrictResponse()
        district_data.set_id(district.id)
        district_data.set_name(district.name)
        district_data.set_code(district.code)
        self.district = district_data
        state_data = StateResponse()
        state = district.state
        state_data.set_id(state.id)
        state_data.set_name(state.name)
        state_data.set_code(state.code)
        self.state = state_data

    def set_state(self, state):
        State_data = StateResponse()
        state = state.state
        State_data.set_id(state.id)
        State_data.set_code(state.code)
        State_data.set_name(state.name)
        self.state = State_data

    def set_city(self, city):
        city_data = CityResponse()
        city_data.set_id(city.id)
        city_data.set_code(city.code)
        city_data.set_name(city.name)
        self.city = city_data

    def set_no(self, no):
        self.no = no

    def set_newpi(self, no, city, district):
        self.no = no + '--' + city.name + '--' + district.name