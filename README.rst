Django-wysihtml5
================

By Daniel Rus Morales <http://danir.us/>

* http://pypi.python.org/pypi/django-wysihtml5/
* http://github.com/danirus/django-wysihtml5/

Simple Django app that provides a Wysihtml5 rich text editor textarea widget.

Includes a **demo project** and a **test suite**. If you commit code, please consider adding proper coverage (especially if it has a chance for a regression) in the test suite.

Run the tests with:  ``python setup.py test``


Quick start
===========

1. Add ``wysihtml5`` to ``INSTALLED_APPS`` in your settings module.
2. Create a model with a field of type ``Wysihtml5TextField``.
3. Create an admin class for that model by inheriting from both ``wysihtml5.admin.AdminWysihtml5TextFieldMixin`` and Django's ``admin.ModelAdmin``.
4. Hit your app's admin URL and see the `wysihtml5 <https://github.com/xing/wysihtml5>`_ editor in action.
