from rest_framework.test import APIRequestFactory
from rest_framework.test import APITestCase
from api.models import Organization


from django.test import TestCase


class ApiTest(APITestCase):

    def test_get_orgs(self):

        url = reverse('/api/orgs/teste')
        data = {}
        response = self.client.get(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

        url = reverse('/api/orgs/abscc')
        data = {}
        response = self.client.get(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

        url = reverse('/api/orgs/galaxycats')
        data = {}
        response = self.client.get(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Organization.objects.count(), 1)
        self.assertEqual(json.loads(response.content), { 'login': 'galaxycats', 'name': 'Galaxy Cats','score': 45})

        url = reverse('/api/orgs')
        data = {}
        response = self.client.get(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content), [{ 'login': 'galaxycats', 'name': 'Galaxy Cats','score': 45}])

        url = reverse('/api/orgs/collectiveidea')
        data = {}
        response = self.client.get(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Organization.objects.count(), 2)
        self.assertEqual(json.loads(response.content), { 'login': 'collectiveidea', 'name': 'Collective Idea','score': 165})

         url = reverse('/api/orgs')
        data = {}
        response = self.client.get(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content), [{ 'login': 'collectiveidea', 'name': 'Collective Idea','score': 165}, { 'login': 'galaxycats', 'name': 'Galaxy Cats','score': 45}])


    def teste_delete_orgs_teste(self):

        url = reverse('/api/orgs/teste')
        data = {}
        response = self.client.delete(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

        url = reverse('/api/orgs/galaxycats')
        data = {}
        response = self.client.get(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Organization.objects.count(), 1)

        
        url = reverse('/api/orgs/collectiveidea')
        data = {}
        response = self.client.delete(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Organization.objects.count(), 0)

        

