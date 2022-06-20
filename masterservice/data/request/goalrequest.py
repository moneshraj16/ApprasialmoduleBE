class GoalRequest:
    def fetch_id(self,obj):
        if 'id' in obj:
            return obj['id']
        else:
            return

    def fetch_request(self, user_obj):
        data = dict()
        if 'id' in user_obj:
            data['id'] = user_obj['id']
        if 'goal' in user_obj:
            data['goal'] = user_obj['goal']
        if 'description' in user_obj:
            data['description'] = user_obj['description']
        if 'grade' in user_obj:
            data['grade'] = user_obj['grade']
        if 'designation_id' in user_obj:
            data['designation_id'] = user_obj['designation_id']
        if 'name' in user_obj:
            data['name'] = user_obj['name']

        return data