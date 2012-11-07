"""
django-wysihtml5 - Simple Django app that allows using the rich text editor Wysihtml5 in text fields.
"""
VERSION = (1, 0, 0, 'a', 1) # following PEP 386

def get_version():
    version = '%s.%s' % (VERSION[0], VERSION[1])
    if VERSION[2]:
        version = '%s.%s' % (version, VERSION[2])
    if VERSION[3] != 'f':
        version = '%s%s%s' % (version, VERSION[3], VERSION[4])
    return version
