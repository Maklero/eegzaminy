import json
from tests.base import ResourceTestCase, skip

class TestGreetingResource(ResourceTestCase):

    def test_response_status(self):
        response = self.client.get('/v1/')
        response_status = response.status_code

        self.assertEqual(response_status, 200)


    def test_response_content_type(self):
        response = self.client.get('/v1/')
        response_content_type = response.content_type

        self.assertEqual(response_content_type, 'application/json')


    def test_response_data(self):
        response = self.client.get('/v1/')
        response_data = response.data
        response_data = json.loads(response_data)

        # Response data structure
        msg = response_data['msg']
        exams_list_url = response_data['exams_list_url']
        exam_url = response_data['exam_url']

        self.assertNotEqual(msg, '')
        self.assertNotEqual(exams_list_url, '')
        self.assertNotEqual(exam_url, '')