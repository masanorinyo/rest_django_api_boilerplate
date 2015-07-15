# DJANGO RESTful API - Example

## API structure

The applicatiom is based on  <a href=http://jsonapi.org/>JSON API</a>

*JSON API allows developers to create a RESTful API and it provides efficiently caching responses, sometimes eliminating network requests entirely.

## Environment setup

##### POW
- Install <a href="http://pow.cx/">POW</a> by running the following command

        curl get.pow.cx | sh

    * pow serves the app locally and allows developers to access it using the app folder's name as a domain name
    

- Then run pow server 

        sh /{project folder}/powconfig.sh

##### Virtualenv

- Install virtualenv in order to set up an independent environment

        pip install virtualenv


- Create a project folder and create a virtual env

        cd your_project_folder
        bin/mkvirtualenv {virtual_env_name}


- Activate the created virtual env

        source bin/activate


##### Python modules
    
- Install all the python modules into the vrtualenv

        pip install -r /{your_project_folder}/requirements.txt

## Database setup


- Install PostgresSQL database

        brew install postgres
        
        # or if you don't use homebrew
        
        sudo apt-get install libpq-dev python-dev
        sudo apt-get install postgresql postgresql-contrib

- Once you install postgres, setup a database with the following commands:

        sudo su - postgres
        
        createdb {database name}
        
        createuser -P 
        
    *You will now be met with a series of 6 prompts. The first one will ask you for the name of the new user. Use whatever name you would like. The next two prompts are for your password and confirmation of password for the new user. For the last 3 prompts just enter "n" and hit "enter". This just ensures your new users only has access to what you give it access to and nothing else.
    
- activate the PostgresSQL


        psql
        

- grant this new user access to your new database with this command:


        GRANT ALL PRIVILEGES ON DATABASE {database name} TO {user name};



## Quick start

1. make sure you are working on an independent virtual platform

        workon {virtualenv}

2. modify the database configuration according to your database admin setup. Go to settings.py inside project main folder. Then edit the following code:


        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.postgresql_psycopg2',
                'NAME': '{database name you set up}',
                "USER" : "{database user name}",
                "PASSWORD" : "{database user password}",
                "PORT" : "5432"
            }
        }


3. Migrate database tables

        ./manage.py migrate


4. Start a server

        ./manage.py runserver

## How to access the API

##### Web application

- API 
    
    You can interact with API in GUI. You can access the site with the following link.
    
        http://api.{name of your folder}.dev

- Admin

    Likewise you can access the admin page which allows you to deal with administrative tasks such as granting other users an access to database and so forth.
    
        http://admin.{name of your folder}.dev

- Default django 

    Without any subdomain, the default django app GUI will be displayed
    
        http://{name of your folder}.dev


##### HTTP request

- Any client that can make a HTTP request can access to API data. However, you cann't access Admin resources.
- When you make a HTTP request, make sure to add the content-type. The following is an example to make a HTTP request to get "user" data.

        
        curl -H "accept: application/vdn.bespoke.{ api version - (ex) v2 }+json" http://api.{name of your app folder}.dev/
        
        
    *depends on the version name, the returned data will be in a variant structure



## Folder Structure

The example code structure is based on 4 components

- api: view and serializer code found inside each version folder
- resources: each resource (app) found with the follwoing 5 files
    1. migrations
    2. models
    3. fixture ( used by test script in order to seed test data in database)
    4. test     
- project name folder: you will find project level configuration 
- templates: you will find custom template files inside this folder

#### IMPORTANT
- Django application requires every folder to have "__init__.py"


## Development process




##### modify the way API returns data

- you can do so by modifying each serializer.py of resource folder inside API version folder

    * ex) api/v2/users/serializers.py


##### add a new resource

- make a new resource (app)

        # make a folder first
        mkdir ./resources/{resource name}
        
        # add django module in there
        django-admin.py startapp {resource name} ./resources/{resource name}

        # once you create an app, add the app to INSTALLED_APPS in settings.py
    

##### Interaction with Database

- How to migrate database
    
    1. make changes in models.py
    2. create a new migration file 
    
        ./manage.py makemigrations {resource name}
        
        
    3. apply those changes to the database.
    
        ./manage.py migrate {resource name}


- removing all data from the database

        ./manage.py flush
        
        
- if you have structural modifications in the database, do the following:

        manage.py sqlclear appname | python manage.py dbshell
        manage.py syncdb 



## Testing

- Each test script is located under app folder. You can run all the test scripts by running the following command.


        sniffer
        
    *Once you run "sniffer", it will re-run the test script whenever you make changes to the code.  If you are using MacOS,  you will get notified when all tests are passed. When sniffer detects any errors, it will output the error logs in the console. **<warning> you won't get notified with error messages through OS notification.