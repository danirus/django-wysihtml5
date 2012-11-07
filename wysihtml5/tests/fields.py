#-*- coding: utf-8 -*-

from django import forms
from django.test import TestCase as DjangoTestCase

from wysihtml5.tests.models import ModelTest


class Wysihtml5TextFieldTestCase(DjangoTestCase):

    def setUp(self):
        self.object = ModelTest.objects.create(first_text="Hello", second_text="World")

    def test_widget_for_wysihtml5textfield_model_field(self):
        class FormTest(forms.ModelForm):
            class Meta:
                model = ModelTest
            
        form = FormTest()
        first_field = form.fields.get("first_text")
        second_field = form.fields.get("second_text")
        self.assert_(first_field.widget.__class__.__name__ == "Textarea")
        self.assert_(second_field.widget.__class__.__name__ == "Wysihtml5AdminTextareaWidget")
