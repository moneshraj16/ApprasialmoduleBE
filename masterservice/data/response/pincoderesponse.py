import json


class PincodeResponse:
    id, district_id, city_id, no = (None,)*4

    def get(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)

    def set_id(self, id):
        self.id = id

    def set_district_id(self, district_id):
        self.district_id = district_id

    def set_city_id(self, city_id):
        self.city_id = city_id

    def set_no(self, no):
        self.no = no