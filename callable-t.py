#!/usr/bin/env python
# encoding: utf-8


class ConfigType(object):

    BASE_TYPES = (None,)

    def is_base_type(self, other):
        return isinstance(other, self.BASE_TYPES)

class Boolean(ConfigType):

    """Boolean type.

    Values are case insensitive and can be set using
    1/0, yes/no, true/false or on/off.
    """
    TRUE_VALUES = ['true', '1', 'on', 'yes']
    FALSE_VALUES = ['false', '0', 'off', 'no']
    BASE_TYPES = (bool,)

    def __call__(self, value):
        if isinstance(value, bool):
            return value

        s = value.lower()
        if s in self.TRUE_VALUES:
            return True
        elif s in self.FALSE_VALUES:

            return False
        else:
            raise ValueError('Unexpected boolean value %r' % value)

    def __repr__(self):
        return 'Boolean'

    def __eq__(self, other):
        return self.__class__ == other.__class__





print callable(Boolean)
boo = Boolean()
boo("yes")
print repr(boo)






class toto(object):
    def __init__(self,name=None):
        self.name = name

    def  __call__(self):
        return self.name

print callable(toto)
matong = toto("haha")
print matong()
