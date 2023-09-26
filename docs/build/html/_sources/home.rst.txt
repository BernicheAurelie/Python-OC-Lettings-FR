Home
====

Home page with society informations and links to profiles and lettings.


get home page
-----------------

The ``index()`` function is called on url:

.. py:function:: index(request)

   Return the home page.

   :param request: automatically filled with url "/"
   :type request: request
   :return: The index template.
   :rtype: view

Exception handlers
------------------

The ``handler404(request, * args, ** argv)`` function is called
when an error 404 occures, like url "/not_found/"

.. py:function:: handler404(request, *args, **argv)

    Return a custom 404 error page

    :param request: automatically filled with wrong url
    :param * args: variable number of non keyword arguments
    :param ** argv: others non keyword arguments send with request

The ``handler500(request, * args, ** argv)`` function is called
when an error 500 occures, an internal error server.

.. py:function:: handler500(request, *args, **argv)

    Return a custom 500 error page

    :param request: automatically filled with url
    :param * args: variable number of non keyword arguments
    :param ** argv: others non keyword arguments send with request
