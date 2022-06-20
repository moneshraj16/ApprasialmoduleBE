class CityRequest:
    def fetch_id(self,obj):
        if 'id' in obj:
            return obj['id']
        else:
            return

    def fetch_request(self, user_obj):
        data = dict()

        if 'id' in user_obj:
            data['id'] = user_obj['id']

        if 'name' in user_obj:
            data['name'] = user_obj['name']

        if 'state_id' in user_obj:
            data['state_id'] = user_obj['state_id']

        return data

