Django a python web framework supports geospatial data. In this post, we will setup the geospatial framework of Django which is [GeoDjango](https://docs.djangoproject.com/en/1.10/ref/contrib/gis/). We will utilize PostGIS a plugin for Postgresql as our main geospatial database.

### Requirements
- Ubuntu 16.04 LTS
- PostgreSQL 9.5
- PostGIS 2.2

### System Setup
1. Install system dependencies: `sudo apt-get install -y python-psycopg2 python-dev python-virtualenv python-pip postgresql postgresql-contrib postgis`
2. Create a user role for PostgreSQL database: `sudo -u postgres bash -c "psql -c \"CREATE USER geouser WITH PASSWORD 'geodbpassword';\""`
3. Change the user role of geouser: `sudo -u postgres bash -c "psql -c \"ALTER ROLE geouser WITH SUPERUSER;\""`
4. Create a PostgreSQL database and set the owner to geouser: `sudo -u postgres createdb -O geouser geodb -E utf-8`
5. Create a virtual environment: `virtualenv env`
6. Activate the virtual environment: `. env/bin/activate`
7. Install Django: `pip install django psycopg2`

### GeoDjango Configuration
1. Create a Django project: `django-admin.py startproject geoapp`
2. Go into the created directory: `cd geoapp`
3. In your text editor open *geoapp/settings*: `nano geoapp/settings`
4. Find and configure the database parameters. It should look like the following:
    
        DATABASES = {
            'default': {
                'ENGINE': 'django.contrib.gis.db.backends.postgis',
                'NAME': 'geodb',
                'USER': 'geouser',
                'PASSWORD': 'geodbpassword',
                'HOST': '127.0.0.1',
                'PORT': '5432'
            }
        }
5. Apply migrations: `python manage.py migrate`

Finally, we have configured and setup our environment. In the next post, we will enable the `Django admin` together with its mapping and geospatial components. 


