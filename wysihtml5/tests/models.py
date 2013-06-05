#-*- coding: utf-8 -*-

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

from wysihtml5.fields import Wysihtml5TextField

@python_2_unicode_compatible
class ModelTest(models.Model):
    first_text = models.TextField()
    second_text = Wysihtml5TextField()
