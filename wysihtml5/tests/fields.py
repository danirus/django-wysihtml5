#-*- coding: utf-8 -*-
try:
    from BeautifulSoup import BeautifulSoup, NavigableString
except ImportError:
    from beautifulsoup import BeautifulSoup, NavigableString

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
                u'A text with all the tags is coming here'
                u'<h1>Header 1</h1>'
                u'<h2>Header 2</h2>'
                u'<h3>Header 3</h3>'
                u'<h4>Header 4</h4>'
                u'<h5>Header 5</h5>'
                u'<h6>Header 6</h6>'
                u'<h7>Header 7</h7>'
                u'<div>A DIV Element</div>'
                u'<p>A Paragraph</p>'
                u'<b>A B Element</b>'
                u'<i>An I Element</i>'
                u'<u>An U Element</u>'
                u'<ul>An UL Element<li>And a LI Element</li></ul>'
                u'<ol>An OL Element<li>And a LI Element</li></ol>'
                u'<span>A SPAN element</span>'
                u'<img src="http://blahblahbla.png">'
                u'<a href="#">An Anchor Element</a>'
                u'<blockquote>Quoting a quote!</blockquote>'

                # Disallowed Tags
                u'<script>alert("this should not stay!")</script>'
                u'<h7>A H7 header?</h7>'))
        self.obj = ModelTest.objects.get(pk=1)
        
    def test_keeptags_keep_the_allowed_tags(self):
        soup = BeautifulSoup(self.obj.second_text)
        self.assert_(soup.first("h1") != None)
        self.assert_(soup.first("h2") != None)
        self.assert_(soup.first("h3") != None)
        self.assert_(soup.first("h4") != None)
        self.assert_(soup.first("h5") != None)
        self.assert_(soup.first("h6") != None)
        self.assert_(soup.first("div") != None)
        self.assert_(soup.first("p") != None)
        self.assert_(soup.first("b") != None)
        self.assert_(soup.first("i") != None)
        self.assert_(soup.first("u") != None)
        self.assert_(soup.first("ul") != None)
        self.assert_(soup.first("ol") != None)
        self.assert_(soup.first("span") != None)
        self.assert_(soup.first("img") != None)
        self.assert_(soup.first("a") != None)
        self.assert_(soup.first("blockquote") != None)

    def test_keeptags_removes_not_specified_tags(self):
        soup = BeautifulSoup(self.obj.second_text)
        self.assert_(soup.first("script") == None)
        self.assert_(soup.first("h7") == None)
