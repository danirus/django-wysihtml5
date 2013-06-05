#-*- coding: utf-8 -*-
from __future__ import unicode_literals

from bs4 import BeautifulSoup, NavigableString

from django import forms
from django.forms.models import modelform_factory
from django.forms.widgets import Textarea
from django.test import TestCase as DjangoTestCase

from wysihtml5.tests.models import ModelTest
from wysihtml5.widgets import Wysihtml5TextareaWidget


class Wysihtml5TextFieldTestCase(DjangoTestCase):
    def test_widget_for_wysihtml5textfield_model_field(self):
        form = modelform_factory(ModelTest)()
        first_widget = form.fields.get("first_text").widget
        second_widget = form.fields.get("second_text").widget
        self.assertEqual(first_widget.__class__, Textarea)
        self.assertEqual(second_widget.__class__, Wysihtml5TextareaWidget)


class KeepTagsTestCase(DjangoTestCase):
    # Test this in the browser and example site by disabling JavaScript
    def setUp(self):
        ModelTest.objects.create(
            first_text="Something not important here", 
            second_text=(
                # Allowed Tags:
                'A text with all the tags is coming here'
                '<h1>Header 1</h1>'
                '<h2>Header 2</h2>'
                '<h3>Header 3</h3>'
                '<h4>Header 4</h4>'
                '<h5>Header 5</h5>'
                '<h6>Header 6</h6>'
                '<h7>Header 7</h7>'
                '<div>A DIV Element</div>'
                '<p>A Paragraph</p>'
                '<b>A B Element</b>'
                '<i>An I Element</i>'
                '<u>An U Element</u>'
                '<ul>An UL Element<li>And a LI Element</li></ul>'
                '<ol>An OL Element<li>And a LI Element</li></ol>'
                '<span>A SPAN element</span>'
                '<img src="http://blahblahbla.png">'
                '<a href="#">An Anchor Element</a>'
                '<blockquote>Quoting a quote!</blockquote>'

                # Disallowed Tags
                '<script>alert("this should not stay!")</script>'
                '<h7>A H7 header?</h7>'))
        self.obj = ModelTest.objects.get(pk=1)
        
    def test_keeptags_keep_the_allowed_tags(self):
        soup = BeautifulSoup(self.obj.second_text)
        self.assert_(soup.find("h1") != None)
        self.assert_(soup.find("h2") != None)
        self.assert_(soup.find("h3") != None)
        self.assert_(soup.find("h4") != None)
        self.assert_(soup.find("h5") != None)
        self.assert_(soup.find("h6") != None)
        self.assert_(soup.find("div") != None)
        self.assert_(soup.find("p") != None)
        self.assert_(soup.find("b") != None)
        self.assert_(soup.find("i") != None)
        self.assert_(soup.find("u") != None)
        self.assert_(soup.find("ul") != None)
        self.assert_(soup.find("ol") != None)
        self.assert_(soup.find("span") != None)
        self.assert_(soup.find("img") != None)
        self.assert_(soup.find("a") != None)
        self.assert_(soup.find("blockquote") != None)

    def test_keeptags_removes_not_specified_tags(self):
        soup = BeautifulSoup(self.obj.second_text)
        self.assert_(soup.find("script") == None)
        self.assert_(soup.find("h7") == None)
