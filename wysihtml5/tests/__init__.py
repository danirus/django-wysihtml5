#-*- coding: utf-8 -*-

import os
import sys
import unittest

def setup_django_settings():
    os.chdir(os.path.join(os.path.dirname(__file__), ".."))
    sys.path.insert(0, os.getcwd())
    os.environ["DJANGO_SETTINGS_MODULE"] = "tests.settings"


def run_tests():
    if not os.environ.get("DJANGO_SETTINGS_MODULE", False):
        setup_django_settings()

    from django.conf import settings
    from django.test.utils import get_runner

    runner = get_runner(settings, "django.test.simple.DjangoTestSuiteRunner")
    test_suite = runner(verbosity=2, interactive=True, failfast=False)
    test_suite.run_tests(["wysihtml5"])


def suite():
    if not os.environ.get("DJANGO_SETTINGS_MODULE", False):
        setup_django_settings()
    else:
        from django.db.models.loading import load_app
        from django.conf import settings
        settings.INSTALLED_APPS = list(settings.INSTALLED_APPS) + \
                                  ['wysihtml5.tests']
        map(load_app, settings.INSTALLED_APPS)

    from wysihtml5.tests import fields, widgets

    testsuite = unittest.TestSuite([
        unittest.TestLoader().loadTestsFromModule(fields),
        unittest.TestLoader().loadTestsFromModule(widgets),
    ])
    return testsuite


if __name__ == "__main__":
    run_tests()
