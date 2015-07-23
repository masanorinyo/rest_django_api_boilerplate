from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from models import Snippet
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from rest_api_example.custom  import utilities
import json

class SnippetTests_v2(APITestCase):

  fixtures = ['test.json']

  def setUp(self):
    self.client.login(username='admin', password='testtest')
    

  def test_get_snippets(self):
    """
    Ensure we can get a list of new snippet objects.
    """    
    url = reverse('api:v2:snippet-list')
    # self._create_snippets(10)
    response = self.client.get(url, format='json')
    # print response
    length = len(response.data['results'])
    self.assertEqual(length, 9)

  def test_create_snippet(self):
    """
    Ensure we can create a new snippet object.
    """    
    url = reverse('api:v2:snippet-list')
    response = self.client.post(url, {"code":"test"}, format='json')
    self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    self.assertTrue(status.is_success(response.status_code))

  def test_show_a_snippet(self):
    """
    Ensure we can get a snippet object.
    """    
    url = reverse('api:v2:snippet-detail', args=[1])
    response = json.loads(self.client.get(url).content)
    self.assertEqual(response['data']['id'], 1)
    self.assertEqual(response['data']['type'], 'snippets')
    self.assertEqual(response['data']['attribute']['code'], 'test')


  def test_put_snippet(self):
    """
    Ensure we can update a existing snippet object.
    """    
    prev_data = {'code':'test'}
    updated_data = {'code':'updated_test'}
    url = reverse('api:v2:snippet-detail', args=[1])
    prev_response = json.loads(self.client.get(url, format='json').content)
    after_response = json.loads(self.client.put(url, updated_data , format='json').content)
    self.assertEqual(prev_response['data']['attribute']['code'], "test")
    self.assertEqual(updated_data['code'], after_response['data']['attribute']['code'])

  def test_delete_snippet(self):
    """
    Ensure we can delete new snippet object.
    """    
    url = reverse('api:v2:snippet-detail', args=[1])
    response = self.client.delete(url, format='json')
    after_response = self.client.get(url, format='json')
    self.assertEqual(response.status_code, 204)
    self.assertEqual(after_response.status_code, 404)
