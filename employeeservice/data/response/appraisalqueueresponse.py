import json


class AppraisalQueueResponse:
    id, appraisal_id, from_user_id, to_user_id, comments = (None,) * 5

    def get(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

    def set_id(self, id):
        self.id = id

    def set_appraisal_id(self, appraisal_id):
        self.appraisal_id = appraisal_id

    def set_from_user_id(self, from_user_id):
        self.from_user_id = from_user_id

    def set_to_user_id(self, to_user_id):
        self.to_user_id = to_user_id

    def set_comments(self, comments):
        self.comments = comments