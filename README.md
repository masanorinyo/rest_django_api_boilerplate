# rest_django_api_boilerplate
pip install -r requirements.txt

find . -iname "*.pyc" | xargs rm


python manage.py reset appname
python manage.py graph_models -a -o rest_api_example.png

./manage.py flush


def test_create_snippet(self):
    """
    Ensure we can create a new snippet object.
    """    
    url = reverse('api:v2:snippet-list')
    response = self.client.post(url, {"code":"test"}, format='json')
    self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    self.assertTrue(status.is_success(response.status_code))