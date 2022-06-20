class GoalMappingRequest:
    id, sub_goal, grade, designation_id, goal_id = (None,)*5

    def __init__(self, user_obj):
        if 'id' in user_obj:
            self.id = user_obj['id']
        if 'sub_goal' in user_obj:
            self.sub_goal = user_obj['sub_goal']
        if 'grade' in user_obj:
            self.grade = user_obj['grade']
        if 'designation_id' in user_obj:
            self.designation_id = user_obj['designation_id']
        if 'goal_id' in user_obj:
            self.goal_id = user_obj['goal_id']

    def get_id(self):
        return self.id

    def get_sub_goal(self):
        return self.sub_goal

    def get_grade(self):
        return self.grade

    def get_designation_id(self):
        return self.designation_id

    def get_goal_id(self):
        return self.goal_id


    # def fetch_id(self, obj):
    #     if 'id' in obj:
    #         return obj['id']
    #     else:
    #         return
    #
    # def fetch_request(self, user_obj):
    #     data = dict()
    #     if 'id' in user_obj:
    #         data['id'] = user_obj['id']
    #     if 'sub_goal' in user_obj:
    #         data['sub_goal'] = user_obj['sub_goal']
    #     if 'grade' in user_obj:
    #         data['grade'] = user_obj['grade']
    #     if 'designation_id' in user_obj:
    #         data['designation_id'] = user_obj['designation_id']
    #     if 'goal_id' in user_obj:
    #         data['goal_id'] = user_obj['goal_id']
    #
    #     return data
