from ..base import BaseResource


class Greeting(BaseResource):
    def get(self):
        data = {
            'msg': 'Welcome in eegzaminy.pl API!',
            'exams_list_url': 'https://api.eegzaminy.pl/v1/exams/list',
            'exam_url': 'https://api.eegzaminy.pl/v1/exams/{name}',
        }
        return self.response(data)
