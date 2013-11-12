#-*- coding: utf-8 -*-

from django.db import models

from wysihtml5.fields import Wysihtml5TextField

class ModelTest(models.Model):
    first_text = models.TextField()
    second_text = Wysihtml5TextField()
