from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from rest_api_example.custom  import utilities
import json

class UserTests_v2(APITestCase):

  fixtures = ['test.json']

  def setUp(self):
    self.client.login(username='admin', password='testtest')
    

  def test_get_users(self):
    """
    Ensure we can get a list of new snippet objects.
    """
    url = reverse('api:v2:user-list')
    # self._create_snippets(10)
    response = self.client.get(url, format='json')
    # print response
    length = len(response.data['results'])
    self.assertEqual(length, 1)

  def test_show_a_user(self):
    """
    Ensure we can get a user object.
    """    
    url = reverse('api:v2:user-detail', args=[1])
    response = json.loads(self.client.get(url).content)
    self.assertEqual(response['data']['id'], 1)
    self.assertEqual(response['data']['type'], 'users')
    
  def test_show_related_snippets(self):
    """
    Ensure we can get relationship data of a user object.
    """    
    url = reverse('api:v2:user-detail', args=[1])
    response = json.loads(self.client.get(url, format='json').content)
    relationships = response['data']['relationships'][0]
    for key, value in relationships.iteritems():
      self.assertEqual(key, "snippets")
      self.assertEqual(len(value['data']), 10)

  def test_show_included_snippets(self):
    """
    Ensure we can get included data of a user object.
    """    
    url = reverse('api:v2:user-detail', args=[1])
    url = url + "?included=snippets"
    response = json.loads(self.client.get(url, format='json').content)
    included_obj =  response['data']['included'][0]
    self.assertEqual(included_obj["id"], 1)
    self.assertEqual(included_obj["type"], "snippets")
    self.assertEqual(included_obj["attribute"]["code"], "test")

  def test_show_related_object(self):
    """
    Ensure we can get relationship data of a user object.
    """    
    url = reverse('api:v2:snippet_relationships', args=[1])
    response = json.loads(self.client.get(url, format='json').content)
    relationships = response['data']
    self.assertEqual(relationships[0]['model_type'], "snippets")
    self.assertEqual(len(relationships), 10)

  def test_show_included_object(self):
    """
    Ensure we can get included data of a user object.
    """    
    url = reverse('api:v2:snippet_included', args=[1])
    response = json.loads(self.client.get(url, format='json').content)
    self.assertEqual(response['data'][0]['attribute']['code'], 'test')
    self.assertEqual(len(response['data']), 10)