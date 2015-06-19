# rest_django_api_boilerplate
pip install -r requirements.txt

find . -iname "*.pyc" | xargs rm


python manage.py reset appname
python manage.py graph_models -a -o rest_api_example.png

./manage.py flush