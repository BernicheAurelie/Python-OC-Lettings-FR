database SQLite3
----------------

Connect to database in sqlite shell:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: console

    $ .open oc-lettings-site.sqlite3

Run queries to display datas:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* View tables: ``.tables``

.. code-block:: console

    $ .tables

* Show column in a table: 

.. code-block:: console

    $ pragma table_info(profiles_profile);

.. NOTE::

    It will return a table with differents fields of the selected table:

    +-----+---------------+-------------+---------+------------+---+
    | cid | name          | type        | notnull | dflt_value | pk|
    +=====+===============+=============+=========+============+===+
    | 0   | id            | integer     | 1       | null       | 1 |
    +-----+---------------+-------------+---------+------------+---+
    | 1   | favorite_city | varchar(64) | 1       | null       | 0 |
    +-----+---------------+--+----------+---------+------------+---+
    | 2   | user_id       | integer     | 1       | null       | 0 |
    +-----+---------------+-------------+---------+------------+---+

* Select user(s) in profile table where favorite city ends with "s":

.. code-block:: console

    $ select user_id, favorite_city from profiles_profile where favorite_city like '%s';

.. NOTE::

    Return:

    +---------+---------------+
    | user_id | favorite_city |
    +=========+===============+
    | 5       | Buenos Aires  |
    +---------+---------------+

* Select address id in letting table where title start with "Joshua%":

.. code-block:: console

    $ select address_id from lettings_letting where title like 'Joshua%';

.. NOTE::

    Return:

    +------------+
    | address_id |
    +============+
    | 1          |
    +------------+

* Select address name in letting address table where id is 1:

.. code-block:: console

    $ Select number, street, city from lettings_address where id is 1;

.. NOTE::

    Return:

    +--------+----------------+-----------+
    | number |     street     |   city    |
    +========+================+===========+
    | 7217   | Bedford Street | Brunswick |
    +--------+----------------+-----------+

* table lettings_address:

    * id
    * number
    * street
    * city
    * state
    * zip_code
    * country_iso_code

* table lettings_letting:

    * id
    * title
    * address_id

* table profiles_profile

    * id
    * favorite_city
    * user_id
