First Step
===========

Prerequisites
-------------

You need:

* GitHub account to clone this repository
* Git CLI
* SQLite3 CLI
* Python interpretor, version ≥ 3.6

.. _installation:

Installation
------------

To use oc lettings site, first clone repo from github:

.. code-block:: console

    $ cd /path/to/the/project/folder
.. code-block:: console

    $ git clone https://github.com/OpenClassrooms-Student-Center/Python-OC-Lettings-FR.git

Virtual Environnement
---------------------

Creation:

.. code-block:: console

    $ cd /path/to/Python-OC-Lettings-FR

.. code-block:: console

    $ python -m venv venv

Activation:

* On macOS / Linux / Git Bash:

.. code-block:: console

    $ source venv/bin/activate

* On Windows Powershell:

.. code-block:: console

    $ env\Scripts\activate

Project start
-------------

.. _start:

Packages installation
~~~~~~~~~~~~~~~~~~~~~~

Install required packages from requirements.txt file

.. code-block:: console

    $ pip install --requirement requirements.txt

Start server locally
~~~~~~~~~~~~~~~~~~~~

.. code-block:: console

    $ python manage.py runserver

Go to **http://localhost:8000** on your live server.

You should have running site with differents profils and lettings