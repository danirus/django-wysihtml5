from django.conf import settings as django_settings
from django.utils.functional import LazyObject

from wysihtml5.conf import defaults as app_settings


class LazySettings(LazyObject):
    def _setup(self):
        self._wrapped = Settings(app_settings, django_settings)

def update_dict_in_depth(a, b):
    """Updates dict a in depth with values of dict b (not for sequences)"""
    for k, v in b.iteritems():
        if a.get(k, None) and type(v) == dict:
                update_dict_in_depth(a[k], v)
        else:
            a[k] = v

class Settings(object):
    def __init__(self, *args):
        for item in args:
            for attr in dir(item):
                if attr == attr.upper():
                    setattr(self, attr, getattr(item, attr))

    def __setattr__(self, name, value):
        obj_attr = getattr(self, name, None)
        if obj_attr and type(obj_attr) == dict:
            update_dict_in_depth(obj_attr, value)
        else:
            object.__setattr__(self, name, value)

settings = LazySettings()
