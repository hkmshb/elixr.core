"""Defines core functions an classes.
"""

import os


class AttrDict(dict):
    """Represents a dictionary object whose elements can be accessed and set 
    using the dot object notation. Thus in addition to `foo['bar']`, `foo.bar`
    can equally be used.
    """

    def __init__(self, *args, **kwargs):
        super(AttrDict, self).__init__(*args, **kwargs)
    
    def __getattr__(self, key):
        return self.__getitem__(key)
    
    def __setattr__(self, key, value):
        self[key] = value
    
    def __getitem__(self, key):
        return dict.get(self, key, None)
    
    def __getstate__(self):
        return dict(self)
    
    def __setstate__(self, value):
        dict.__init__(self, value)
    
    def __repr__(self):
        return '<AttrDict %s>' % dict.__repr__(self)
    
    @staticmethod
    def make(obj):
        """Converts all dict-like elements to a storage object.
        """
        if not isinstance(obj, (dict,)):
            raise ValueError('obj must be a dict or dict-like object')

        _make = lambda d: AttrDict({ k: d[k]
            if not isinstance(d[k], (dict, AttrDict))
            else _make(d[k])
                for k in d.keys()
        })
        return _make(obj)
