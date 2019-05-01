import json
from tests.base import ResourceTestCase, skip


class TestExamListResource(ResourceTestCase):


    def test_response_status(self):
        response = self.client.get('/v1/exams/list')
        response_status = response.status_code

        self.assertEqual(response_status, 200)


    def test_response_content_type(self):
        response = self.client.get('/v1/exams/list')
        response_content_type = response.content_type

        self.assertEqual(response_content_type, 'application/json')

    
    def test_response_data(self):
        response = self.client.get('/v1/exams/list')
        response_data = response.data
        response_data = json.loads(response_data)

        # Response data structure
        list_exam = response_data['list']

        self.assertNotEqual(len(list_exam), 0)


class TestExamResource(ResourceTestCase):


    def test_response_status(self):
        response = self.client.get('/v1/exams/ee09')
        response_status = response.status_code

        self.assertEqual(response_status, 200)

    
    def test_response_content_type(self):
        response = self.client.get('/v1/exams/ee09')
        response_content_type = response.content_type

        self.assertEqual(response_content_type, 'application/json')

    def test_response_data(self):
        response = self.client.get('/v1/exams/ee09')
        response_data = response.data
        response_data = json.loads(response_data)

        # Response data strcuture
        title = response_data['title']
        questions = response_data['questions']

        self.assertEqual(title, 'ee09')
        self.assertNotEqual(len(questions), 0)


    def test_not_found_exam(self):
        response = self.client.get('/v1/exams/dawdawdwad')
        response_status = response.status_code

        self.assertEqual(response_status, 404)

class TestVerificationResource(ResourceTestCase):


    @skip('Not implemented.')
    def test_response_status(self):
        pass

    @skip('Not implemented.')
    def test_response_content_type(self):
        pass

    @skip('Not implemented.')
    def test_response_data(self):
        pass