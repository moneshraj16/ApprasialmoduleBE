class StateRequest:
    def fetch_id(self, obj):
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

        if 'country_id' in user_obj:
            data['country_id'] = user_obj['country_id']

        return data