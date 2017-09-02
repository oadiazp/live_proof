from collections import OrderedDict

from django.utils.functional import cached_property


class NamedChoices(tuple):
    """
    Model Field Choices.

    Use it to represent choices of a model field:

        >>> CHOICES = NamedChoices((
        ...    ('NAME', 'name'),
        ...    ('HOUSE', 'house'),
        ... ))

        >>> 'HOUSE' in CHOICES
        True

        >>> CHOICES.HOUSE
        'HOUSE'

        >>> CHOICES['NAME']
        'NAME'

        >>> CHOICES[0]
        ('NAME', 'name')

        >>> CHOICES.dict['NAME']
        'name'

    """

    def __init__(self, iterable=None, *args, **kwargs):
        tuple.__init__(iterable, *args, **kwargs)
        self._keys = frozenset(k for k, v in iterable)

    def __getitem__(self, key, *args, **kwargs):
        if key in self._keys:
            return key
        return super().__getitem__(key, *args, **kwargs)

    def __contains__(self, key):
        return key in self._keys or super().__contains__(key)

    def __getattr__(self, attr):
        # the __setstate__ thing is here to avoid problems with `copy.copy`
        if attr != '__setstate__' and attr in self._keys:
            return attr
        raise AttributeError(
            'Object %s does not have attribute "%s"' % (
                self, attr
            )
        )

    @cached_property
    def dict(self):
        return OrderedDict(self)

    @cached_property
    def max_length(self):
        return max(len(key) for key in self.dict)
