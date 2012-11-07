#-*- coding: utf-8 -*-

from django.db.models import fields

from wysihtml5.widgets import Wysihtml5AdminTextareaWidget


class Wysihtml5TextField(fields.TextField):

    def formfield(self, **kwargs):
        defaults = {"widget": Wysihtml5AdminTextareaWidget}
        defaults.update(kwargs)
        return super(Wysihtml5TextField, self).formfield(**defaults)

try:
    from south.modelsinspector import add_introspection_rules
    add_introspection_rules([], ["^wysihtml5\.fields\.Wysihtml5TextField"])
except ImportError:
    pass
