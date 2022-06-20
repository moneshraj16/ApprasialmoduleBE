class AppraisalQueueRequest:
    id, appraisal_id, from_user_id, to_user_id, comments = (None,)*5

    def __init__(self,user_obj):
        if 'id' in user_obj:
            self.id = user_obj['id']
        if 'appraisal_id' in user_obj:
            self.appraisal_id = user_obj['appraisal_id']
        if 'from_user_id' in user_obj:
            self.from_user_id = user_obj['from_user_id']
        if 'to_user_id' in user_obj:
            self.to_user_id = user_obj['to_user_id']
        if 'comments' in user_obj:
            self.comments = user_obj['comments']


    def get_id(self):
        return self.id

    def get_appraisal_id(self):
        return self.appraisal_id

    def get_from_user_id(self):
        return self.from_user_id

    def get_to_user_id(self):
        return self.to_user_id

    def get_comments(self):
        return self.comments

