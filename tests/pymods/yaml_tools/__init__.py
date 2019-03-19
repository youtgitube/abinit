'''
    This package gather all tools used by the Abinit test suite for
    manipulating YAML formated data.
'''
from __future__ import print_function, division, unicode_literals

try:
    import yaml
    import numpy  # numpy is also required
    import pandas

    is_available = True

except ImportError:
    is_available = False


class CorruptedDocument(object):
    '''
        Replace the YAML parser output when it fail.
    '''
    # trick to workaround the custom sys.path
    _is_corrupted_doc = True

    def __init__(self, error, context=''):
        self.error = error
        self.context = context

    def __repr__(self):
        return "<Corrupted document {}: {}>".format(
            self.error.__class__.__name__, str(self.error))


if is_available:

    def yaml_parse(content, catch=True, *args, **kwargs):
        from . import structures
        if catch:
            try:
                return yaml.load(content, *args, **kwargs)
            except yaml.YAMLError as e:
                return CorruptedDocument(e, context=content)
        else:
            return yaml.load(content, *args, **kwargs)

    yaml_print = yaml.dump
