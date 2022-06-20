class PincodeRequest:
    def fetch_id(self, obj):
        if 'id' in obj:
            return obj['id']
        else:
            return

    def fetch_request(self, user_obj):
        data = dict()
        if 'id' in user_obj:
            data['id'] = user_obj['id']

        if 'district_id' in user_obj:
            data['district_id'] = user_obj['district_id']

        if 'city_id' in user_obj:
            data['city_id'] = user_obj['city_id']

        if 'no' in user_obj:
            data['no'] = user_obj['no']

        return data

