# BucketList API

A simple Django Rest framework implementation that implements `authentication` and `authorization`.

### Setup

Setup is simple, ensure you have **virtualenv** setup on your local development machine and create a virtual environment

```bash
$ virtualenv -p python3 venv
# or if you prefer
$ virtualenv venv
$ . venv/bin/activate

# install requirements
(venv) $ pip install -r requirements.txt
```
> This will create a virtual environment and setup the dependencies.

After which you will need to perform a migration with this command

```bash
$ python manage.py makemigrations
$ python manage.py migrate
```
> This sets up a small database with sqlite3 and creates the tables and V1 of the database

Afterwards you can optionally create a super user

```bash
$ python manage.py createsuperuser
````
> Enter the credentials as prompted

Now you can run the server with

```bash
python manage.py runserver
```

Browse on this address on your browser [http://127.0.0.1:8000/bucketlists/](http://127.0.0.1:8000/bucketlists/)

You will be prompted for a username and password, enter the ones you created in the `createsuperuser` command.

[![forthebadge](http://forthebadge.com/images/badges/made-with-python.svg)](http://forthebadge.com)
[![forthebadge](http://forthebadge.com/images/badges/built-by-developers.svg)](http://forthebadge.com)
[![forthebadge](http://forthebadge.com/images/badges/built-with-love.svg)](http://forthebadge.com)