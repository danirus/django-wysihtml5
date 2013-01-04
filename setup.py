from setuptools import setup, find_packages
from setuptools.command.test import test

def run_tests(*args):
    from wysihtml5.tests import run_tests
    run_tests()

test.run_tests = run_tests

setup(
    name = "django-wysihtml5",
    version = "1.0a2",
    packages = find_packages(),
    include_package_data = True,
    license = "MIT",
    description = "Simple Django app that provides a Wysihtml5 rich text editor textarea widget.",
    long_description = "Simple Django app that provides a Wysihtml5 rich text editor textarea widget, with a complete command toolbar to give HTML format to your documents.",
    author = "Daniel Rus Morales",
    author_email = "inbox@danir.us",
    maintainer = "Daniel Rus Morales",
    maintainer_email = "inbox@danir.us",
    url = "http://pypi.python.org/pypi/django-wysihtml5/",
    classifiers = [
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
    test_suite = "dummy",
)
