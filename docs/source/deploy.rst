Deployment
==========

Dockerfile
----------

Le dockerfile sera utilisé par docker pour créer notre image:
Dockerfile will be used to build our image
* Install and update python3 et postgresql
* Install and update pip
* Install packages in 
* Specify path to copy files
* Manage Staticfiles
* Specify expose port
* Specify server and wsgi app used

Build and push
--------------

Build image run container:

    - ``$ docker build --tag oc_lettings_site:latest .``
    - ``$ docker run --name oc_lettings_site -dp 127.0.0.1:8000:8000 oc_lettings_site:latest``

Push to DockerHub:
    - ``$ docker login -u <username>``
    - ``$ docker tag oc_lettings_site <username>/oc_lettings_site``
    - ``$ docker push <username>/oc_lettings_site``


Heroku
------

Create app:

    * ``$ heroku login``
    * ``$ heroku create projet13-oc-lettings-site``
    * ``$ heroku git:remote -a projet13-oc-lettings-site``

Push on heroku:

    * ``$ heroku container:login``
    * ``$ heroku container:push -a projet13-oc-lettings-site web``
    * ``$ heroku container:release -a projet13-oc-lettings-site web``
