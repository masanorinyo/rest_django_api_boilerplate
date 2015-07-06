from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.test import APITestCase, APIClient,APIRequestFactory


class SnippetTests(APITestCase):
  def setUp(self):
    self.factory = APIRequestFactory()
    self.client = APIClient()
    self.user = User.objects.create_user('testuser', email='testuser@test.com', password='testing')
    self.user.save()
    token = Token.objects.create(user=self.user)

    token.save()

  def test_create_snippet(self):
      """
      Ensure we can create a new snippet object.
      """    
      url = reverse('api:v2:snippet-list')
      
      self.client.login(username='testuser', password='testing')      
      # data = {'code': 'DabApps'}
      response = self.client.get(url, format='json')
      print "========== response data start ============"
      print response
      print "========== response data end  ============"
      self.assertTrue(status.is_success(response.status_code))
      # self.assertEqual(response.data, data)
  