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


Demo site
=========

1. Cd into the demo directory: ``cd django-wysihtml5/example/demo``
2. Run syncdb with --no-input: ``python manage.py syncdb --noinput`` (user: admin, pwd: admin)
3. Run the dev web server: ``python manage.py runserver``
4. Hit the demo URL: `http://localhost:8000 <http://localhost:8000>`_ to see the example article fully formatted with Wysihtml5.
5. Hit the demo admin URL: `http://localhost:8000/admin/ <http://localhost:8000/admin/>`_ to see the widget in action.


Customization
=============

You can customize two commands:
* Create Link
* Insert Image

To customize each command create a function to render the dialog and the javascript code to handle the result. Visit the commands wiki pages (`createLink <https://github.com/xing/wysihtml5/wiki/Supported-Commands#wiki-createLink>`_, `insertImage <https://github.com/xing/wysihtml5/wiki/Supported-Commands#wiki-insertImage>`_) to see how. 

Once you have the function edit your settings file and declare the key that corresponds with the command you have customize. The default values are:

* ``WYSIHTML5_FUNC_CREATE_LINK_DIALOG = "wysihtml5.widgets.render_create_link_dialog"``
* ``WYSIHTML5_FUNC_INSERT_IMAGE_DIALOG = "wysihtml5.widgets.render_insert_image_dialog"``


Have questions?

* On Wysihtml5: `go here <https://github.com/xing/wysihtml5>`_
* On this app: `post a comment <http://danir.us/projects/django-wysihtml5-10>`_

Go and make happy your users!
