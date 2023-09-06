Profiles
========

App to manage profiles

get profiles list
-----------------

To retrieve the profiles' list,
you can use the ``profile.index()`` function:

.. py:function:: profile.index(request)

   Return the list of profiles.

   :param request: automatically filled with url "profiles/"
   :type request: request
   :return: The index template with all profiles.
   :rtype: view


get a profile
-------------

To retrieve a profile information,
you can use the ``profile()`` function:

.. py:function:: profile(request, username)

   Return a profile detail, with profile favorite_city
   and associated user's informations

   :param request: automatically filled with url "profiles/<str:username>/"
   :param username: associated username to the selected profile
   :type request: request
   :type username: str()
   :return: The profile template with profile object.
   :rtype: view
