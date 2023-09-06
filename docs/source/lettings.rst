Lettings
========

App to manage lettings and address

get lettings list
-----------------

To retrieve the lettings' list,
you can use the ``letting.index()`` function:

.. py:function:: letting.index(request)

   Return the list of lettings.

   :param request: automatically filled with url "lettings/"
   :type request: request
   :return: The index template with all lettings.
   :rtype: view


get a letting
-------------

To retrieve a letting information,
you can use the ``letting()`` function:

.. py:function:: letting(request, letting_id)

   Return a letting detail, with letting title and letting address

   :param request: automatically filled with url "lettings/<letting_id>/"
   :param letting_id: id of selected letting
   :type request: request
   :type letting_id: int()
   :return: The letting template with letting object.
   :rtype: view
