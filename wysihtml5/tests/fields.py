#-*- coding: utf-8 -*-

from django import forms
from django.forms.widgets import Textarea
from django.test import TestCase as DjangoTestCase

from wysihtml5.tests.models import ModelTest
from wysihtml5.widgets import Wysihtml5AdminTextareaWidget


class Wysihtml5TextFieldTestCase(DjangoTestCase):

    def setUp(self):
        self.object = ModelTest.objects.create(first_text="Hello", 
                                               second_text="World")

    def test_widget_for_wysihtml5textfield_model_field(self):
        class FormTest(forms.ModelForm):
            class Meta:
                model = ModelTest
            
        form = FormTest()
        first_field = form.fields.get("first_text")
        second_field = form.fields.get("second_text")
        self.assertEqual(first_field.widget.__class__, Textarea)
        self.assertEqual(second_field.widget.__class__, 
                         Wysihtml5AdminTextareaWidget)
