import json


class StateResponse:
    id, name, country_id, code = (None,)*4


    def get(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                            sort_keys=True, indent=4)

    def set_id(self, id):
        self.id = id

    def set_name(self, name):
        self.name = name

    def set_country_id(self, country_id):
        self.country_id = country_id

    def set_code(self, code):
        self.code = code
