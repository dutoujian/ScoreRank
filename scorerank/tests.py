import datetime
from django.test import TestCase, RequestFactory, Client
from scorerank.models import ClientInfo

# Create your tests here.
class ClientScoreTests(TestCase):
    def setUp(self):
        self.client = Client()
        ClientInfo.objects.create(client_name="test",score=1,create_time=datetime.datetime.now(),update_time=datetime.datetime.now())
        # self.client_infos = ClientInfo.objects.all().order_by('-score')

    def test_add(self):
        score = ClientInfo.objects.get(client_name="test")
        self.assertEquals(score.score, 1)

    def test_query_view_status_code(self):
        response = self.client.get('/score/query',{'client_name': 'test'})
        self.assertEqual(response.status_code, 200)

    def test_query_view_response(self):
        response = self.client.get('/score/query',{'client_name': 'test'})
        self.assertEqual(response.json()['data'][-1]['client_name'], 'test')

    def test_add_view_status_code(self):
        response = self.client.post('/score/add',{'client_name': 'tt', 'score': 2})
        self.assertEqual(response.status_code, 200)
