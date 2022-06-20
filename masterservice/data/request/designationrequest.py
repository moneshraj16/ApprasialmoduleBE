class DesignationRequest:
    def fetch_id(self, obj):
        if 'id' in obj:
            return obj['id']
        else:
            return

    def fetch_request(self, user_obj):
        data = dict()
        if 'name' in user_obj:
            data['name'] = user_obj['name']
        if 'code' in user_obj:
            data['code'] = user_obj['code']

        return data