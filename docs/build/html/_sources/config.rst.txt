Settings
========

Project Settings 
----------------

* Specify Allowed hosts

    * "127.0.0.1" and "localhost"
    * add 'testserver' for pytest
    * and ".herokuapp.com" or other server

* Installed apps

    * new app lettings
    * new app profiles
    * whithenoise to manage staticfiles

* Staticfiles

    * root: where will be collect staticfiles for deployment
    * url: staticfiles url for server
    * dirs: where django will find static files (to reference it in templates)
    * storage: which engine will be used to collect staticfiles

Admin section
-------------

You can manage users, lettings, address or profiles in admin part:

    * url **"admin/"**
    * username **admin**
    * password **Abc1234!**
