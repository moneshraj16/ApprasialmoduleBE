import json


class AppraisalDetailResponse:
    id, appraisal_id, remarks, rating = (None,) * 4


    def get(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

    def set_id(self, id):
        self.id = id

    def set_appraisal_id(self, appraisal_id):
        self.appraisal_id = appraisal_id

    def set_remarks(self, remarks):
        self.remarks = remarks

    def set_rating(self, rating):
        self.rating = rating