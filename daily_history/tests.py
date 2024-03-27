from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from daily_history.models import Contents


class ContentsCreateAPITest(TestCase):
    client_class: APIClient = APIClient

    @classmethod
    def setUpTestData(cls):
        cls.contents = Contents.objects.create(
            title='test_title',
            detail='test_detail',
        )
        for _ in range(10):
            Contents.objects.create(
                title='test_title',
                detail='test_detail',
            )

    def test_컨텐츠_목록(self):
        with self.assertNumQueries(2):
            response = self.client.get('/daily-history/')
        self.assertEqual(response.status_code, 200)
        response_data = response.json()
        self.assertEqual(len(response_data), 11)
        self.assertEqual(response_data[0]['id'], self.contents.id)
        self.assertEqual(response_data[0]['title'], self.contents.title)
        self.assertEqual(response_data[0]['detail'], self.contents.detail)

    def test_컨텐츠_생성(self):
        request_data = {'title': 'test_title', 'detail': 'test_detail'}
        response = self.client.post('/daily-history/', request_data)
        self.assertTrue(response.status_code, 201)
        response_data = response.json()
        self.assertEqual(response_data['title'], request_data['title'])
        self.assertEqual(response_data['detail'], request_data['detail'])

    def test_컨텐츠_삭제(self):
        response = self.client.delete(f'/daily-history/{self.contents.id}/')
        self.assertEqual(response.status_code, 204)
        self.assertFalse(Contents.objects.filter(id=self.contents.id).exists())

    def test_이미지_생성(self):
        contents = Contents.objects.create(title='test_title', detail='test_detail')
        request_data = {'image': 'image_data', 'contents': contents.id}
        response = self.client.post(f'/daily-history/{contents.id}/image/', request_data)
        self.assertTrue(response.status_code, 201)

    def test_이미지_삭제(self):
        contents = Contents.objects.create(title='test_title', detail='test_detail')
        request_data = {'image': 'image_data', 'contents': contents.id}
        response = self.client.post(f'/daily-history/{contents.id}/image/', request_data)
        self.assertTrue(response.status_code, 201)
        image_id = response.json()['id']
        response = self.client.delete(f'/daily-history/{contents.id}/image/{image_id}', request_data)
        self.assertTrue(response.status_code, 204)
